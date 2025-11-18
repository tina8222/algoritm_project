# def tin():
#   print("EJkfgkhnkkjnjsnxabzbsfdfdkfkdskds")
    
    
# tin()
# tin()
# tin()

# 


# تعریف کردیم داخل فانکشنمون که بهش مقدار بدیم argument در این قسمت ما 
# def function_nam(argument)


# exercise functin

# def passvalidation(password):
#     if len(password) < 8:
#          print("the password must have tinathe least 8 letters")
#     elif password.isnumeric():
#          print("plz enter a password must have least one letter")
#     elif password.isalpha():
#          print("plz enter a password with umber")
#     else:
#          print("ohhh cool you are valid .....")
    
# while True:
#           password = input("enter yor password:")
#           passvalidation(password) 

 
# def me(name,lname,*args):
#      print(f"hello im {name} {lname}")
#      print(f"mewww {args}")
#      print(type({args}))
     
# me("tina","mirdar","mew","mew","mew")

# if you want to use more argument use *
# convert *args to set store


# def tin(*fruites):
#     for x in fruites:
#       print(f"i love {x}")
      
# tin( "apple","cucumber","watermelon","melon")
         

# def mew(fname,lname):
#      print(fname)
#      print(lname)
     
# mew(lname="mirdar",fname="tina")



# def new(fname,lname,*args,**kwargs):
#      print(fname)
#      print(lname)
#      print(args)
#      print(kwargs["age"])
# new("tina","mirdar","mew","meww","mewwww",age="22",city="krj")

# *arges create set
# **kwargs creatw dic




# def mine(lname,name="tina"):
#      print(f"hello {name} {lname}")
     
# mine("mirdar","asal")


# def neww(food):
#      for item in food:
#           print(item)
          
# fruits = ["apple","cucumber","watermelon","melon"] 
# neww(fruits)
# neww("tinamirdar") we can use string
# or
# neww(["apple","cucumber","watermelon","melon"] )




# def num(a,b):
#     c = a + b
#     return c
# print(num(2,3))
    


# def num(a,b):
#     return a + b
# print(num(2,3))



# def num(a,b):
#     return a + b
# mew = num(2,3)
# print(mew)


# def sum(a, b):
#         return a, b
# mew = sum(2, 3)
# print(mew)


# def sum(a, b):
#      a += 1
#      b += 5
     #   c = 26
#      return a, b
# mew = sum(2, 3)
# for item in mew:
#      print(item)


# username = input("plz enter your user: ")


# def vallidation(username):
#      if len(username) > 8:
#           return False
#      else:
#           return True
# if vallidation(username):
#      print("cool its right")
# else:
#      print("noits wrong")


# def mew():
#      pass

# exercise 1

# def myfunc(name):
     
#      upps = 0
#      lows = 0
#      for n in name:
#           if n.isupper():
#                upps += 1
#           elif n.islower():
#                lows += 1
#           else:
#                pass
          
#      print(f"upper case:{upps}")
#      print(f"lower case:{lows}")
    
# while True: 
#      name = input("plz enter your name:")
#      myfunc(name)clear_session_cookies()

# exercise 2



# def numbertype(number):
#      if number % 2 == 0:
#          print(f" {number} is even")
#      else:
#          print(f" {number} is odd")
         
# while True:
     
#      number = int(input("plz enter your number:")) 
#      numbertype(number)

     
     # exercise 3
     


# def converter(day,month,year):
#      if month > 10:
#         birthday = year + 622
#      elif day > 10 and month == 10:
#         birthday = year + 622
#      else:
#         birthday = year + 621
        
#      print(f"your year of birthday is {birthday}")

# day = int(input("plz enter your day:"))
# month = int(input("plz enter your month:"))
# year =int(input("plz enter your year:"))  

# converter(day=day,month=month,year=year)  



# def myfunc(a):
#      return a + 10

# print(myfunc(10))
# myfunc2 = myfunc         
# use variabe to create function
# print(myfunc2(70))


# x = lambda b : b + 10
# print(x(60))
     # lambda is a function with out name

# def myfunc(n):
#      return lambda a: a * n
# mydoubler = myfunc(4)
# print(mydoubler(8))
    
# def myfunc(a):
#     def new(n):
#         return a * n
  
#      return new

# X = myfunc(7)
# print(X(8))


# my_list = [2,4,6,8,9,12]
# my_list2 = [2,4,6,8,9,12]
# # def myfunc(num):
# #     return num * 2

# x = list(map(lambda a,b: a * b,my_list, my_list2))
# print(list(x))
# print(list(x))








