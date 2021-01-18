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
root.title("Mpaz - Escritura en json para historico de archivos publicos")

def write_json(myId, myName, filename="myj_test.json"):
    try:
        with open ("myj_test.json") as json_file:
            data = json.load(json_file)
            temp = data["files"]
            y = {"id": myId, "name": myName, "date": str(date.today().strftime("%d/%m/%Y"))}
            temp.append(y)
        with open (filename, "w") as f:
            json.dump(data, f, indent=4)
        print("Escritura exitosa")
    except:
        print("Fallo en escritura")

write_json("id test", "nombre test")
input("\nCierra esta ventana para salir")