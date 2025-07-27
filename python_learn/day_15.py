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
    
mycursor = mydb.cursor()
# mycursor.execute("show tables")
# mycursor.execute("show columns from student")
insert ="""insert into student(id,full_name,age,address,faculty) 
values(%s,%s,%s,%s,%s)"""
data =[(1,"Nishan Rana",23,"ktm","science"),
       (2,"sagar thapa",21,"lalitpur","management"),
       (3,"hero",24,"bhaktpur","science"),
       ]
mycursor.executemany(insert,data)
mydb.commit()
mycursor.execute("select * from studdent")
result = mycursor.fetchall()
print(result)
# print(f'{mycursor.rowcount} rows inserted')
mycursor.close()
mydb.close()
