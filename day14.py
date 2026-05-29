'''
#modules:a modules in python is a file that contains python code such as variable, functions, class ,statements
#there are two types of modules user defined built-in
#user define
def add (a,b):
    return a+b
def sub(a,b):
    return a-b

#built-in
import math
print(math.sqrt(25))
print(math.factorial(10))
print(math.pow(2,6))

#example:
import math as m
print(math.sqrt(25))
print(math.factorial(10))
print(math.pow(2,6))

#example:os is the communicate with the system
import os
os.mkdir("some_python")

#example
import os
os.remove("demo.txt")
#program

import sys
print(sys.version)
print(sys.exit)
print(sys.path)



#program
import random
print(random.randint(1000,9999))



from collections import Counter,defaultdict
data = ['a','b','c','d']
counter =Counter[data]
print(counter)

dd=defaultdict(int)
dd['missing']+=1
print(dd['missing'])
print(dd)


from collections import Counter,defaultdict
data = ['a','b','c','d']
counter =Counter[data]
print(counter)

dd=defaultdict(int)
dd['missing']+=1
print(dd['missing'])
print(dd)






























