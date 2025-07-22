# super class derived class

# parent class child class

# base class and derived class



# class parent:
#     a = 10 
#     b = 11 
#     def mul(self):
#         return self.a* self.b
# class child(parent):
#     d = 1
#     gretting = "hello"

#     def add(self):
#         return self.a + self.b
    
#     def result(self):
#        return self.add() , self.mul()
        
    
# obj = child()
# print(obj.result())

# class math():
  
#     def __init__(self,a,b):
#          self.a = a
#          self.b = b
        
# class operation(math):
#     def add(self):
#         return self.a + self.b
#     def mul(self):
#         return self.a * self.b
#     def dev(self):
#         return self.a / self.b
# obj = operation(15,3)
# print(obj.add())
# print(obj.mul())
# print(obj.dev())


# class University():
   
#     def init(self):
#         self.name_uni = "Pokhara University"
#         self.addr_uni = "Pokhara"
#         pass
 
#     def uni_info(self):
#         print("Name of University : ",self.name_uni)
#         print("Addr of University : ",self.addr_uni)
 
# class College(University):
 
#     def init(self):
#         super().init()
#         self.name_colle = "NCIT"
#         self.code_colle = 1234
 
#     def college_info(self):
#         print(f"Name of colllege : {self.name_colle}")
#         print(f"Code of college : :{self.code_colle}")
 
# class Student(College):
 
#     def init(self):
#         super().init()
#         self.name_stu = "Bishal Bista"
#         self.roll = 123456
 
#     def stu_profile(self):
#         print(f"Name of student : {self.name_stu}")
#         print(f"Roll of student : {self.roll}")
#         self.college_info()
#         self.uni_info()
 
 
# obj1 = Student()
# obj1.stu_profile()
        
        



        
    
        
    


# private and public class

# class employee:
#     def __init__(self):
#         self.name = "Nishan"

# obj = employee()
# print(obj.name)

#     __name ="Nishan"
#     address = "koteshwor"
    
    
#     def __private_method(self):
#         return "This is a private method."

#     def public_method(self):
#         return self.__private_method()  

# obj = MyClass()
# print(obj.public_method())  
# print(obj.__private_method())  


# class Parent():
#     __private_att = 6
#     public_att = 60


#     def __private(self):
#         return "i am private"

#     def public_private(self):
#         return self.__private()

# class Child(Parent):

#     def test(self):
#         return self.__private()

# obj = Child()
# print(obj.public_att)

