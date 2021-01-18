#imports api
#imports api drive

from __future__ import print_function
import re
import pickle
import os
import os.path
import xml.etree.cElementTree as ET
import json
import smtplib
import cryptocode
from datetime import date
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from apiclient import errors
from apiclient.http import MediaFileUpload

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.appdata']

#imports entorno
from tkinter import Tk, Canvas, Frame, Label, Entry, Button, W, E, Listbox, END
import psycopg2

root = Tk()
root.title("Mpaz - MeliTest - Test de envio de mail y armado de password encriptada")

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
        print("Fallo la generacion del password")     


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
        print("Mail enviado correctamente")
    except:
        print("Error en el envio de mail")

#ESPECIFICAR ACA EL MAIL DE DESTINO
send_email("test","test","mati.g.paz@gmail.com")
input("\nCierra esta ventana para salir")