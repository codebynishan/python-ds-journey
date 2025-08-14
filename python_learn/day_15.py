# Run this in Python shell
import mysql.connector
print(mysql.connector.__version__) 
from tabulate import tabulate

mydb = mysql.connector.connect(
    host ="localhost",
    user ="root",
    port =3306,
    password ="Nishan@2059",
    database ="school"
    
    
)
if mydb.is_connected:
    print("connection successfull....")
else:
    print("error....")
    
mycursor = mydb.cursor()

# mycursor.execute("show columns from student")

# for column in mycursor.fetchall():
#     print(column)


insert ="insert into student(id,name,age,address,faculty)values(%s,%s,%s,%s,%s)"
data = [(111,'nishan rana',23,'ktm','science'),
        (222,'sagar thapa',20,'lalitpur','management')]
mycursor.executemany(insert,data)
mydb.commit()

mycursor.execute("select * from student")
result = mycursor.fetchall()

header = "id","name","age","address","faculty"
print(tabulate(result,headers=header,tablefmt="grid"))
print(result)


