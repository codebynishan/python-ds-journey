# Run this in Python shell
import mysql.connector
print(mysql.connector.__version__) 

mydb = mysql.connector.connect(
    host ="localhost",
    user ="root",
    port =3307,
    database ="school"
)
if mydb.is_connected:
    print("connection successfull....")
else:
    print("error....")
    

