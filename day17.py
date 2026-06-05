#inheritance:this allows one class to aquire the properties and methods of anothers class
#types of inheritance are there single,multiple,multi-level,hierarcal,hybride
#single:a class inherts from a single parent class
class father:
    def land(self):
        print("My father has 10A")
        
class sai(father):
    def my_own(self):
        print("I own 5A")
fam=sai()
fam.land()

#multiple:a class of more than one 
class mother:
    def gold(self):
        print("My mother have 1kg G")
class son(father,mother):
    def mine(self):
        print("I have ntg")
all_=son()
all_.land()
all_.gold()

#multi level:a class inherts from a parent  class and another class inherts from than child class
class grandfather:
    def land(self):
        print("My grand father have 5A of land")
class father( grandfather):
    def land(self):
        print("have flat at BNG ")
class sson:
     def Ntg(self):
        print("I own both of their p")
        
all_=son()
all_.land()
all_.gold()

#hierarcal:multiple child classes inherts from a single parent
class father :
    def Land(self):
        print("10 A  land")
class sai(father) :
    def sis(self):
        print("jobless")
rag=sai()
rag.Land()



#hybrids:this is the combinations of two or more types of inheritance
class A:
    def so(self):
        print('class A')
class B(A):
    def som(self):
        print('class B')
class C(A):
    def s(self):
        print('class C')
class D(B,C):
    def some(self):
        print('class D')
        
how =D()
how.so()

#super method:is used to access  methods and constructor of the parent class
class parent:
    def display(self):
        print('Method parent')
class child (parent):
    def display(self):
        super().display()
        print('Method child')
any_=child()
any_.display()

class person:
    def __init__(self,name):
        self.name=name

class stu_(person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll=roll
    def show(self):
         print(f"Name:(self.name)")
         print(f"Roll no:(self.roll)")
any_=stu_("sai",266)
any_.show()













        









    







        

        
                








        


        








    














