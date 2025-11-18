class person:
    def __init__(self):
        self.a = 5 #public
        self._b = 14 #protected
        self.__c = 19 #private
    # def test(self):
    #     print(self.__c)  
        
o1 = person()
# print(o1.a)  #we can access and change it
# o1.a = 15
# print(o1.a)

# print(o1._b) #we can access onley in inerihance class 
# print(o1.__c) # you cant access it
# o1.test()
# o1.__c = 20
# print(o1.__c) # this isnt our private variable




# class person:
#     def __init__(self):
#         self.a = 5 #public
#         self._b = 14 #protected
#         self.__c = 19 #private
        
#     def getter(self):
#         return self.__c
    
#     def setter(self,value):
#         self.__c = value
        
#     def del_age(self):
#         del self.__c
    
    
#     age = property(getter,setter,del_age)
    
# # p1 = person()
# # print(p1.getter())

# # a = p1.setter(38)
# # print(p1.getter())
# p1 = person()
# print(p1.age)
# p1.age = 68
# print(p1.age)
# del p1.age
# print(p1.age)




# class person:
#     def __init__(self):
#         self.a = 5 #public
#         self._b = 14 #protected
#         self.__c = 19 #private
        
#     @property    
    
#     def getter(self):
#         return self.__c
    
#     def setter(self,value):
#         self.__c = value
        
#     def del_age(self):
#         del self.__c

# p1= person()
# print(p1.del_age)



class person:
    def __init__(self):
        self.a = 5 #public
        self._b = 14 #protected
        self.__c = 19 #private
        
    @property    
    def age(self):
        return self.__c
    @age.setter
    def age(self,value):
        if value >40:
            raise ValueError("sorryyyyyyyyyyyyyy")
        self.__c = value
    @age.deleter    
    def age(self):
        del self.__c

p1 = person()
print(p1.age)
p1.age = 54
print(p1.age)
