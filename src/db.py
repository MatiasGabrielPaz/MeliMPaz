 # ----- Example Python program to create a database in PostgreSQL using Psycopg2 -----

# import the PostgreSQL client for Python

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect("user=postgres password='postgres'")
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

cursor          = conn.cursor()
query = "SELECT datname FROM pg_catalog.pg_database WHERE lower(datname) = lower('drive')"
cursor.execute(query)
dbExist = cursor.fetchone()
conn.commit()
conn.close()
if dbExist:
    conn = psycopg2.connect(dbname="drive", user="postgres", password="postgres", host="localhost", port="5432")
    cursor = conn.cursor()
    query = "SELECT * FROM drive"
    myV = 0
    try:
        cursor.execute(query)
    except:
        myV = 1
    conn.commit()
    conn.close()
    if myV == 0:
        print("exite todo")
    else:
        conn = psycopg2.connect(dbname="drive", user="postgres", password="postgres", host="localhost", port="5432")
        cursor = conn.cursor()
        query = "CREATE TABLE drive(id text, nombre text, extension text, owner text, visibilidad text, fecha text);"
        cursor.execute(query)
        conn.commit()
        conn.close()
else:
    conn = psycopg2.connect("user=postgres password='postgres'")
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor          = conn.cursor()
    name_Database   = "drive"
    sqlCreateDatabase = "create database "+name_Database+";"
    cursor.execute(sqlCreateDatabase)
    conn.commit()
    conn.close()
    conn = psycopg2.connect(dbname="drive", user="postgres", password="postgres", host="localhost", port="5432")
    cursor = conn.cursor()
    query = "CREATE TABLE drive(id text, nombre text, extension text, owner text, visibilidad text, fecha text);"
    cursor.execute(query)
    conn.commit()
    conn.close()

input("Estado de base de datos: CORRECTO. Presione cualquier tecla para continuar")



# wasdwqwqewqeqwewqewqeweq





#  # ----- Example Python program to create a database in PostgreSQL using Psycopg2 -----

# # import the PostgreSQL client for Python

# import psycopg2

# from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


# con = psycopg2.connect("user=postgres password='postgres'")
# con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

 

# # Obtain a DB Cursor
# cursor          = con.cursor()
# name_Database   = "drive"
 

# # Create table statement
# sqlCreateDatabase = "create database "+name_Database+";"

# papa = "SELECT datname FROM pg_catalog.pg_database WHERE lower(datname) = lower('drive')"
# # Create a table in PostgreSQL database
# cursor.execute(papa)
# myVar = cursor.fetchone()
# if myVar:
#     print("asdadsds")
# con.commit()
# con.close()














# # cursor.execute(sqlCreateDatabase)
# # con.commit()
# # con.close()


# conn = psycopg2.connect("user=postgres password='postgres'")
# conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

 

# # Obtain a DB Cursor
# cursor          = conn.cursor()

 

# # Create table statement

# cursor = conn.cursor()
# query = "select exists(select * from information_schema.tables where table_name='drive')"
# cursor.execute(query)
# myVar = cursor.fetchone()

# print(myVar)
# conn.commit()
# conn.close()
# input("Press enter to exit ;)")








