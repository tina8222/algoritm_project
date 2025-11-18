# def hello(name):
    
#     def hello_amir():
#         print(f"hello {name}")
        
    
#     return hello_amir


# x = hello("tina")
# x()





# def hello_decorators(func):
      
      
#       def inner(*args,**kwargs):
#             print("befor the function")
#             func(*args,**kwargs)
#             print("after your function")
             
             
#       return inner





# @hello_decorators
# def hello(name):
#       print(f"hi user {name} ")
    
# hello("tina")



# def updecorators(func):
#       def inner(*args,**kwargs):
#           x = func(*args,**kwargs)  
#           return x.upper()
        
        
#       return inner



# @updecorators
# def test(name):
#       return f"hello {name}"
    
# x = test("tina")
# print(x)

# import time

# def time_decorators(func):
#       def wrapper(*args,**kwargs):
#             begin = time.time()
#             func(*args,**kwargs)
#             end = time.time()
#             print(f"total time : {end - begin}")
      
#       return wrapper
      

# @time_decorators
# def test(name,lastname):
#       time.sleep(5)
#       print(f"hello {name} {lastname}")
      
# test("tina","mirdar")


# def dec(func):
#     def inner():
#       x = func()
#       return x * 3
    
#     return inner


# def dec2(func):
#       def inner():
#             x = func()
#             return x * 10
#       return inner


# @dec2
# @dec
# def test():
#       return 5
# print(test())
















