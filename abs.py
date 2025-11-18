from abc import ABC,abstractmethod,abstractproperty

class Animal(ABC):
    
    @abstractmethod
    def move(self):
        pass
    
    @abstractproperty
    def legs(self):
        pass
    
    
class lion(Animal):
    def move(self):
        print("lion is moving")
    def legs(self):
        return 4
    
    
class Dog(Animal):
    def move(self):
        print("dog is moving")
    def legs(self):
        return 6
    
l1 = lion()
d1 = Dog()

l1.move()
d1.move()
print(l1.legs())
print(d1.legs())
