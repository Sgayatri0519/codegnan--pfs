#list comrehension:offers a shortest syntax when we want to create a new list from existing list
#syntax:vari_name=[epression loop condition]

old_=[1,2,3,4,5]
new_=[so for  so in old_]
print(new_)

old_=[1,2,3,4,5]
new_=[so for  so in old_ if so%2==0]
print(new_)

#write a program of even  or odd place

old_=[1,2,3,4,5,6,7]
new_=[so if so%2!=0 else "even" for so in old_]
print(new_)

#generators:a generatorsbb in python are special type of itterable,allowing users to iterate over data efficiently without storing everything in memory.they generate values lazily using yield keyword.
#why we use gen :
#1.generators do not store the entire dataset in memory, they generator value on the fly runtime.
#2.to advoiding the unnecessary storage  of data speed up excution.
#how it works:it works like normal function but uses the yield keyword instead of return.when the function is called,it does not excute immediately instead,it return  a generator object which can be iterated using loop or the next()function
def simple_gen():
    print("start")
    yield 1
    yield 2
    yield 3
    yield 4
    print("end")
gen=simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

def any(num):
   for i in range (1,num+1):
       yeild (i*i)
a=any(5)
print(next(a))
'''
#write a program of normal form
def any(num):
   for i in range (1,num+1):
       result.append(i*i)
      result result
  print(sqr(5))
'''
#write a program of print consonsts
so="every placement is a dream fulfilled"
any=''
for j in so :
    if j not in 'AEIOUaeiou':
        any+=j
print(any)

  





          


