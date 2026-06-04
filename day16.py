#oops object oriented programming system :is a programming paradigm that organizes code around objects rather than just functions and procedures. An object combines data (attributes) and behavior (methods) into a single unit.
#how many types of oops
'''
#class :class is a blue print are a template used to create object

class stu_:
  def edu(self):  
    print("I am studying B.tech")
  def sports(self):
    print("cricket")
          
s1=stu_()

#object:an object is an instance of class

class stu_:
    name='sai'
s1=stu_()
print(s1.name)

#attributes:are the variables that belongs to a class or an object


class stu_:
    name='sai'
    age=21
s1=stu_()
print(s1.name)
print(s1.age)

#methods the function defined inside the class is methods
class PFS_DA:
    def python(self):
        PFS_DA='Batch_03'
        print('this is PFS and DA batch03')
        
    def flask(self):
         PFS='Batch_03'
         print('this is pfs batch03')
all_=PFS_DA()
all_.python()
all_.flask()

#construction : (__init__):is a special method that is automatically called when an object is created

class ATM:
    def __init__(self,Balance,name):
        self.Balance=Balance
        self.name=name
    def Balance_(self):
         print(f"{self.name} your total balance is {self.Balance+700}")
    def name_(self):
        print(self.name)

card=ATM(Balance=50000,name='sai')
card.Bal_check()
card.name_()

#access specifies
# 1.public: this can be accessed from anywhere in the program(_)
class stu:
    __name='sai'

s1=stu()
print(s1._stu__name)

# 2.protect: this is represented using a single underscore(_)
class stu:
    __name='sai'

s1=stu()
print(s1._stu__name)
 
 
# 3.private:this is represented using a single underscore(__)
 

class stu:
    __name='sai'

s1=stu()
print(s1._stu__name)

#Encapsulation:is the process of binding data and methods together
'''

class Bank:
  def __init__(self,balance):
     self.__balance=balance=balance
  def depo_(self,amount ):
     self.__balance +=amount
  def get_bala(self):
     return self.__balance
acc=Bank(1000)
acc.depo_(10000)
print(acc.get_bala())
     
     

















     


         
















         



               
      


