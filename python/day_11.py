# python class

# class test:
#     x = 5
# obj = test()
# print(obj.x)


    
# class person:
#     name = "Nishan"
#     age = 23
#     occ = "student"
#     def info(self):
#         print(f"{self.name} is {self.occ}")
# obj = person()
# obj1 = person()
# obj.name ="sagar"
# obj1.name ="Binod"
# print(obj.name)
# obj.info()
# obj1.info()


# class person:
#     def __init__(self,name,age):
#         print("this is init ")
#         self.name = name
#         self.age = age
#     def info(self):
#         print(f'{self.name} is {self.age}years old')
# obj = person("Nishan",23)
# obj.info()

# class student:
#     def __init__(self):
#         print("adding new student in database....")
# obj = student()    

# class test():
#      a ="hello"
# obj = test()
# print(obj)

# class math():
#     a = 50
#     b = 60
    
#     def __str__(self):
#         return "this is str method"
#     def add(self):
#        return self.a +self.b
    
#     def mul(self):
#         return self.add()*3
    
# obj = math()
# print(obj)
# print(obj.add())
# print(obj.mul())
    
    
# class test3():
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#         print("i am init")
#         return
#     def test(self):
#         print(self.num)


# class math():
#     a = 20
#     b = 30
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#         return 

#     def add(self):
#         return self.a + self.b
#     def mul(self):
#         return self.add()*3
# obj = math()
# print(obj.add())
# print(obj.nul())

# class student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
        
#     def get_avg(self):
#             sum = 0
#             for val in self.marks:
#                 sum += val
#             print("hi",self.name,"your avg score is :",sum/3)
            
# s1 = student("Nishan rana",[99,78,90])
# s1.get_avg()
# s1.name = "sagar"
# s1.get_avg


# class account:
#     def __init__(self,bal,acc):
#         self.balance = bal
#         self.account_no = acc
     
#     def debit(self,amount):
#         self.balance -= amount
#         print("Rs",amount,"was debited")
#         print("total balance =",self.get_balance())
        
#     def credit(self,amount):
#         self.balance += amount
#         print("Rs",amount,"was credited")
#         print("total balance =",self.get_balance())
    
#     def get_balance(self):
#         return self.balance
                   
# acc1 = account(10000,12345)
# acc1.debit(1000)
# acc1.credit(500)




    
    
