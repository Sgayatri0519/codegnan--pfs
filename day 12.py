#built in functions

print()
input()
len()
type()
max()
min()

#sort 
n=[1,2,3,4,5]
n.sort()
print(n)

#sorted
m=[9,8,7,6,5]
m.sorted()
print(m)

#recursive functions:a recurvise function that calls itself to solve a problem by breaking it into small or simple sub problem
#example:
def fac(num):
    if num==1:
        return 1
    return num*fac(num-1)
print(fac(5))

#write a program of patterns
patt=100
count=0
for i in range(2,patt+1):
    if i==2:
        continue
    for j in range(2,i+1):
        count=+1
        print(j,end=" ")
    print()

#write a program of even or odd
    num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

#write a program of what is your name
name=intput("enter a name:")
print("enter your name:")

#return:this ends a function excution and sends a value back to the code that called the function
#ex:

def add(a,b):
  return a+b
res=add(4,5)
print(res)



#lambda functions:a lambda function is a small anonamus functions.lambda can take n number of arguments,but only one expression
#syntax:lambda arguments: expression

so=lambda a,b:a+b
print(so(3,4,5))

so=lambda x,y:x*y
print(so(3,4,5))





