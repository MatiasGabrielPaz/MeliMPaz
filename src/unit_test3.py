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
root.title("Mpaz - conexion con base de datos postgres")

def database_connection():
    try:
        conn = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host="localhost", port="5432")
        cursor = conn.cursor()
        print("Conexion con la base de datos exitosa")
    except:
        print("Error en la conexion con la base de datos")


database_connection()
input("\nCierra esta ventana para salir")