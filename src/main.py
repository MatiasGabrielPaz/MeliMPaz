from __future__ import print_function
import re
import pickle
import os
import os.path
import xml.etree.cElementTree as ET
import json
import smtplib
import cryptocode
import pandas as pd
from datetime import date
from datetime import datetime
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from apiclient import errors
from apiclient.http import MediaFileUpload

SCOPES = ['https://www.googleapis.com/auth/drive']

from tkinter import Tk, Canvas, Frame, Label, Entry, Button, W, E, Listbox, END
import psycopg2

root = Tk()
root.title("Mpaz - MeliTest")
    
def authenticate():
    try:
        creds = None
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        if not creds or not creds.valid: #si no hay credenciales, te manda a logearte
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0) #guarda las credenciales para corridas futuras
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        return build('drive', 'v3', credentials=creds) #return
        write_log("Conexion exitosa con Google Drive Api V3")
    except:
        write_log("ERROR: Conexion fallida con Google Drive Api V3")
        return "0"

def write_log(texto):
    try:
        try:
            file1 = open("log.txt","a")
            file1.write("\n" + datetime.now().strftime("%Y-%m-%d %H:%M:%S ") + texto)
            file1.close() 
        except:
            print("No se encuentra el archivo de log")
    except:
        print("Fallo en la escritura de logs")

def bring_password():
    try:
        f = open("first_half.txt", "r")
        firstHalf = str(f.read())
        r = open("second_half.txt", "r")
        secondHalf = str(r.read())
        complete = firstHalf + secondHalf
        decoded = cryptocode.decrypt(complete, "mypassword")
        return decoded
    except:
        write_log("ERROR: Fallo la generacion del password") 

def bring_db_password():
    try:
        f = open("pass_db.txt", "r")
        myPass = str(f.read())
        return myPass
    except:
        write_log("ERROR: Fallo al buscar la password de la DB") 


def send_email(subject, msg, mail):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        EMAIL_ADDRESS = "melitestmpaz@gmail.com"
        PASSWORD = bring_password()
        server.login(EMAIL_ADDRESS, PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(mail, mail, message)
        server.quit()
        write_log("Mail enviado correctamente a " + mail) 
    except:
        write_log("ERROR: Error en el envio de mail") 

def execute_query(query):
    try:
        conn = psycopg2.connect(dbname="drive", user="postgres", password=str(bring_db_password()), host="localhost", port="5432")
        cursor = conn.cursor()
        cursor.execute(query)
        myVar = ""
        try:
            myVar = cursor.fetchone()
        except:
            aaa =  0
        conn.commit()
        conn.close()
        write_log("Se ejecuto la query " + query)
        if (myVar):
            return myVar
    except:
        write_log("ERROR: Error al ejecutar la query " + query)

def write_json(myId, myName, filename="myj.json"):
    try:
        with open ("myj.json") as json_file:
            data = json.load(json_file)
            temp = data["files"]
            y = {"id": myId, "name": myName, "date": str(datetime.now().strftime("%Y-%m-%d %H:%M:%S "))}
            temp.append(y)
        with open (filename, "w") as f:
            json.dump(data, f, indent=4)
    except:
        write_log("ERROR: Fallo en la escritura del json")

def remove_permission(service, file_id, permission_id):
    try:
        service.permissions().delete(fileId=file_id, permissionId=permission_id).execute()
    except:
        write_log("ERROR: Ocurrio un error al intentar borrar el permiso entre el usuario " + str(permission_id) + " y el file " + str(file_id))

def save_csv():
    df = pd.read_json (r'myj.json')
    df.to_csv (r'mycsv.csv', index = None)

def update_database(service):
    write_log(" __       __  ________  __        ______         ______   _______   _______  ")
    write_log("/  \     /  |/        |/  |      /      |       /      \ /       \ /       \ ")
    write_log("$$  \   /$$ |$$$$$$$$/ $$ |      $$$$$$/       /$$$$$$  |$$$$$$$  |$$$$$$$  |")
    write_log("$$$  \ /$$$ |$$ |__    $$ |        $$ |        $$ |__$$ |$$ |__$$ |$$ |__$$ |")
    write_log("$$$$  /$$$$ |$$    |   $$ |        $$ |        $$    $$ |$$    $$/ $$    $$/ ")
    write_log("$$ $$ $$/$$ |$$$$$/    $$ |        $$ |        $$$$$$$$ |$$$$$$$/  $$$$$$$/  ")
    write_log("$$ |$$$/ $$ |$$ |_____ $$ |_____  _$$ |_       $$ |  $$ |$$ |      $$ |      ")
    write_log("$$ | $/  $$ |$$       |$$       |/ $$   |      $$ |  $$ |$$ |      $$ |      ")
    write_log("$$/      $$/ $$$$$$$$/ $$$$$$$$/ $$$$$$/       $$/   $$/ $$/       $$/       ")
    write_log("")
    # Call the Drive v3 API
    results = service.files().list(fields="nextPageToken, files(id, name, fullFileExtension, owners(displayName), modifiedTime, shared, fullFileExtension, mimeType, owners(permissionId), owners(emailAddress))").execute()
    items = results.get('files', [])
    if not items:
        write_log("No se encontraron archivos")
    else:
        for item in items:
            myShared = item['shared']
            if myShared == True: #Si el archivo es publico..
                resultados = service.permissions().list(fileId=item['id'], fields="nextPageToken, permissions(id)").execute()
                permisos = resultados.get('permissions', [])
                permisosRemovidos = ""
                for permiso in permisos : #por cada permiso
                    if permiso["id"] != item['owners'][0]['permissionId'] : #si el permiso es distinto al owner
                        remove_permission(service,item["id"],permiso["id"]) #remueve el permiso. TODOPodriamos agregar la validacion de si el owner no soy yo
                        write_json(str(item['id']), str(item['name'])) #escribe en json historico
                        write_log("Se removio el permiso del usuario " + str(permiso["id"]) + " en el archivo " + str(item["name"]) + " (" + str(item["id"]) + ")")
                        permisosRemovidos = permisosRemovidos + " " + str(permiso["id"])
                if permisosRemovidos != "" :
                    send_email("MeliApp", "Se removieron los permisos de los usuarios " + permisosRemovidos + " del archivo " + str(item["name"]) + " (" + str(item["id"]) + ")", str(item['owners'][0]['emailAddress']))
            myVar = execute_query("SELECT nombre FROM drive WHERE id = '" + item['id'] + "'") 
            if not myVar: #si el file no esta en la base de datos..
                try: 
                    execute_query("INSERT INTO drive(id, nombre, extension, owner, visibilidad, fecha) VALUES ( '" + item['id'] + "','" + item['name'] + "','" + item['fullFileExtension'] + "','" + str(item['owners']).split('\'')[3] + "','Privado','" + item['modifiedTime'] + "')")
                except: #entra en la excepcion si el file no tiene extension
                    execute_query("INSERT INTO drive(id, nombre, extension, owner, visibilidad, fecha) VALUES ( '" + item['id'] + "','" + item['name'] + "','-','" + str(item['owners']).split('\'')[3] + "','Privado','" + item['modifiedTime'] + "')")
            else: #entra si el file ya esta en la base de datos
                myFecha = execute_query("SELECT fecha FROM drive WHERE id = '" + item['id'] + "'")
                if str(myFecha).split('\'')[1] != item['modifiedTime']: #si la fecha de la bd difiere de la del drive
                    print(str(myFecha).split('\'')[1])
                    print(item['modifiedTime'])
                    try:
                        execute_query("UPDATE drive SET nombre= '" + item['name'] + "', extension= '" + item['fullFileExtension'] + "', owner= '" + str(item['owners']).split('\'')[3] + "', visibilidad= 'Privado', fecha= '" + item['modifiedTime'] + "' WHERE id= '" + item['id'] + "'")
                    except:
                        execute_query("UPDATE drive SET nombre= '" + item['name'] + "', extension= '-', owner= '" + str(item['owners']).split('\'')[3] + "', visibilidad= 'Privado', fecha= '" + item['modifiedTime'] + "' WHERE id= '" + item['id'] + "'")
                     

def main():
    os.system("db.py")
    service = authenticate()
    update_database(service)
    save_csv()

    input("Press enter to exit ;)")

if __name__ == '__main__':
    #Canva
    canvas = Canvas(root, height=500, width=1000)
    canvas.pack()
    main()

