#polymorphism:this means many forms it allows the same function,methods,or operator to behave differntly depending on the object
#there are three types:
#method overloading:it means defining multiple methods with the same name but different paramaters
#example
class calcu_:
    def add(self,a,b,c=0):
        return a+b+c
An=calcu_()
print(An.add(23,6))
print(An.add(23,6,34))
#example
class calcu_:
    def add(self,a,b):
        return a+b
    def add(self,a,b,c=0):
         return a+b+c
An=calcu_()
print(An.add(23,6))
print(An.add(23,6,34))
#method overriding:this occurs when a child class provides its own implemtation of method already 
class animal:
     def sound(self):
        print("Animal makes sound")
class dog(animal):
     def sound(self):
        print("dogs barks")
nt=dog()
nt.sound()           
#operator overloading:this allows operator such as +,-,* etc,,to perform different actions for user-defined objects
#note:the operator inside the method will overload a special method or operator given in the call 
class std:
    def __init__(self,marks):
          self.marks=marks
    def __add__(self,other):
        return self.marks+other.marks
so1=std(4)
so=std(78)
print(so1+so)
#Abstraction:this is the of hideing internal implemention details and showing only essential features to the user
#it focuses on what an object does rather than how it does it
from abc import ABC,abstractmethod
class shape(ABC):
   @abstractmethod
   def area(self):
       pass
   def perimeters(self):
       pass
class Rec(shape):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def area(self):
         return self.a*self.b
    def perimeters(self):
         return 2*(self.a*self.b)
an=Rec(10,5)
print(an.area())








        
    





























