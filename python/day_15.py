import _mysql_connector
import mysql


mydb = mysql.connector.connect(
user="root",
host ="localhost",
port =3306,
)
print(mydb)
