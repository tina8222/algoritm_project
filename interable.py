# mylist = ["cucumber","orangr","avacado","mango"]    #iterable
# myiterator = iter(mylist)

# print(next(myiterator))
# print(next(myiterator))
# print(next(myiterator))
# print(next(myiterator))

# mystr = "tinamirdar"
# myiter = iter(mystr)
# print(len(mystr))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))



class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
       if self.a <= 20:
        x = self.a
        self.a += 1
        return x
    
       else:
        raise StopIteration
    
    
myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
     
  print(x)

        












