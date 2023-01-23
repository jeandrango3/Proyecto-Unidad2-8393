#Nos permite ingresar la contraseña de la base de datos 
import getpass
#Nos ayuda a crear conexion con la base de datos 
import oracledb
#Para crear un dataframe 
import pandas as pd
import pandasql as ps
#Ayuda  a la lectura de archivos csv 
import csv

#Declaramos una variable donde se va almacenar la contraseña ingresada
pw = getpass.getpass("Enter password: ")

#Establece conexion con Oracle a traves del usuario y el dsn 
connection = oracledb.connect(
    user="system",
    password=pw,
    dsn="localhost:1521/xe")

print("Conexion exitosa con la base de datos")



# Lee el archivo csv con el ingex borramos la primera columna de datos 
#df = pd.DataFrame(pd.read_csv('Provincia.csv',index_col=0))
#print(df)

#---------------Insercion de datos -------------#
#lee y abre el archivo que se encuentra en la ubicacion 
read =csv.reader(open("C:/Users/Asus/Desktop/Nueva carpeta/Recibe.csv", errors="ignore"))
#Variable que almacena la concexionc on Oracle
cursor = connection.cursor()

#Comienza a leer e ingresar los datos por columnas 
column =[]
for line in read:
      column.append(line)
print("leido")

#Se define la tabla en donde vamoss a ingresar los datos
print("Datos insertados")
for line in column:
   insertar = 'insert into "TBRECIBE" VALUES(:1, :2 ,:3,:4)'
   cursor.execute(insertar, line)

connection.commit()
print("Cargado")
#Se debe cerrar el proceso 
cursor.close() 