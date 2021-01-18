# Meli App Mpaz

Es una aplicación en Python para inventariar en una Base de Datos todos los archivos pertenecientes a la unidad de Drive de un usuario.
Para su utilizacion, una base de datos Postgres es creada desde la aplicación.
La principal funcion de esa aplicacion es analizar un directorio de GoogleDrive y en el caso de encontrar archivos que estén configurados como públicos y puedan ser
accedidos por cualquier persona, los mismos deberan establecerse como privados y enviar un e-mail al owner notificando el cambio realizado.
La aplicación guarda en la base sólo aquellos archivos que no hayan sido almacenados en alguna corrida anterior y actualiza su fecha de modificación o cualquier otro dato.
Ademas, contiene un inventario histórico de todos los archivos que fueron en algún momento públicos.

Para utilizar la aplicacion solo se debera correr el archivo main.py
Ademas se agregaron las siguientes funcionalidades:
-Logs \n
-Tests unitarios de funcionalidades particulares
-Encriptacion y split de password
-Historico de archivos publicos en json
-Historico de archivos publicos en csv

El 

