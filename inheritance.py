# class Person:
#     def __init__(self,name,lastname):
#         self.name = name
#         self.lastname = lastname
        
#     def printname(self):
#         print(self.name,self.lastname)
        
# class student(Person):
#     def __init__(self,name,lastname,age):
#     #    Person.__init__(self,name,lastname)
#        super().__init__(name,lastname)
#        self.age = age
#     def printage(self):
#         print(f"hello im {self.age}")
        
    

# c1 = student("tina","mirdar",22)

# print(c1.age)
# c1.printage()




cs = [
    {
        "titel": "python",
        "teacher": "arezo"
    },
    {
        "titel": "html",
        "teacher": "samane"
    },
    {
        "titel": "js",
        "teacher": "ahmad"
    }
]










class Users:
    def __init__(self,firstname,lastname):
        self.fname = firstname
        self.lname = lastname
        
    def fullname(self):
        print(f"my fullname is {self.fname} {self.lname}")
        
        
class Student(Users):
    def __init__(self, firstname, lastname,email):
        super().__init__(firstname, lastname)
        self.email = email
        self.courses = []
        
    def fullname(self):
        print("hello im from student")
        super().fullname()    
    
    def printcourses(self):
        if self.courses:
            for course in self.courses:
                print(course['titel'])
        else:
            print("erooorrrrrrrrrrrrrrr")
    
    
        
    
class Teacher(Users):
    def __init__(self, firstname, lastname,code):
        super().__init__(firstname, lastname)
        self.code = code
        
    def fullname(self):
        print("im a teacher")
        return super().fullname()
        
s1 = Student("tina","mirdar","tina@gmail.com")
s2 = Student("asal","shokohmand","asal@gmail.com")

s1.courses.append(cs[1])
s2.printcourses()
s1.printcourses()
























