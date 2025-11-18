# class MyClass:
#      x = 9
#      y = 4
# p1 = MyClass()
# p2 = MyClass()

# print(p1.x)
# print(p2.x)
# print(p1.y)


# function init

# class MyClass:
#     def __init__(self):
#         self.name = "amir"

# p1 = MyClass()
# p2 = MyClass()

# print(p1.name)


# class MyClass:
#     def __init__(self, name, lastname):
#         self.myname = name
#         self.mylastname = lastname
        

# p1 = MyClass("tina","mirdar")
# p2 = MyClass("asal","shokohmand")

# print(p1.myname)
# print(p2.mylastname)



# class MyClass:
#     def __init__(self, name, lastname):
#         self.myname = name
#         self.mylastname = lastname
        
#     def fullname(self):
#         print(f"heloo im {self.myname} {self.mylastname}")

# p1 = MyClass("tina","mirdar")
# p2 = MyClass("asal","shokohmand")

# p1.fullname()
# p2.fullname()


# class Person:
#     def __init__(self,age,height):
#         self.myage = age
#         self.Myheight = height
        
#     def mbi(self):
#         print(f"im tina mirdar im {self.myage} years old and im {self.myheight}  kg")

# p1 = Person(22,43)
# p2 = Person(23,65)

# p1.mbi()
# p2.mbi()



# class People:
#     def __init__(self,name,lastname,age):
#         self.name = name
#         self.lastname = lastname
#         self.age = age
        
#     def fullname(self):
#         print(f"hello my name is {self.name} {self.lastname} and im {self.age} years old")
        
# p1 = People("tina","mirdar",22)
        
# p1.fullname()

# p1.age = 15  
# # for modifyv your properties 
# p1.fullname()

# del p1.age
# #  for delete properties

# p1.fullname()



# exercise one 

class Car:
    car_numbers = 0
    def __init__(self,name,price):
        self.name = name
        self.price = price
        self.vaziat = False
        # print(f" {self.name} hello from init")
        Car.car_numbers += 1
        
    def start(self):
        if self.vaziat == False:
            self.vaziat = True
            print(f"{self.name} is startig")
        else:
            print(f"baba mn is on dont starting")
            
    def off(self):
        if self.vaziat == True:
            self.vaziat = False
            print(f"{self.name} is off now")
        else:
            print("the car is off olease start egain")
        

p1 = Car("benz", "9000000")
p2 = Car("peride", "15000000")
p3 = Car("pezho", "15000000")
# p1.start()
# p1.start()
# p1.off()
# p1.off()
p3.car_numbers = 5
Car.car_numbers = 9

print(Car.car_numbers)
print(p2.car_numbers)
print(p1.car_numbers)
print(p3.car_numbers)


