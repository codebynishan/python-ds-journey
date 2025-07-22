# filehandling

'''
file create
file read
file write
file append

read nad write
'''

# open 
# file = open('python/day_10.py',"r")
# print(file.read())
# print(file.readline())
# file.close()

# file = open('python/day_5.md',"r")
# print(file.read())
# file.close()

# write
# file = open('nishan.txt','w')
# print(file.write("hello world"))
# file.close()


# append
# file = open('python/day_5.md',"a")
# print(file.write("hello world....\n This is from file handling"))
# file.close()

# error handling
'''NameError
ZeroDivisionError
IndexError
IndentationError
ValueError
AttributeError'''

# try and except block

a = 10 
   
try:
    print(b)
except NameError:
    print("some thing went wrong")
except ZeroDivisionError:
    print("number canoot be divided by zero")
except FileNotFoundError as e:
    print(e)
except:
    print("undifined error")
    

from datetime import datetime

def write_error_message(msg):

    filename = f'error/{datetime.today().date()}-error.txt'
    f = open(filename,'a')
    f.write(f'{msg}\n')
    f.close()


# try and except block
try:

    # f = open("sudan.py",'r')
    data = data+1
    f = open("sudan.py",'r')
    # data = data+1
    print("test")
except NameError as e:
    write_error_message(e)



