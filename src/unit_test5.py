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
from datetime import datetime
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
root.title("Mpaz - Escritura en log")

def write_log(texto):
    try:
        try:
            file1 = open("log_test.txt","a")
        except:
            print("No se encuentra el archivo de log")
        file1.write("\n" + datetime.now().strftime("%Y-%m-%d %H:%M:%S ") + texto)
        file1.close() 
        print("Escritura exitosa")
    except:
        print("Fallo en escritura")

write_log("texto")
input("\nCierra esta ventana para salir")