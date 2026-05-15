'''# program to convert 24h clock into nrml clock

time_="20:37"
parts_=time_.split(":")
hour_=int(parts_[0])
min_=int(parts_[1])
print(f"(time_) is converted into {hour_-12} :{min_} pm")

#list is collection of different data types
#[] and separate by,

any=[1,"python",[1,2]]
print(any)

#

any =[1,"python",[1,2,[34,"this is python 3rd class",78],"python is language",89],34,[3,4]]
print(any[2])


#methods --append():this method is used to add new item into list and it will in the lst index postions
syntax:variable-name.append(item)


any =[1,2,3]
any.append(6)
print(any)
any.append[(90,20)]
print(any)

#immutable :could not able to modify on that particular variable
#eg:integer ,string

#mutable :can able to modify on that particular variable
#eg:list

so="python is a"
print(so.replace("python","java"))
print(so)
any=[1,2,3]
print(any.append(6))
print(any)

'''
#extend():this method is used to add itterable into list,and it will in the last index postion,each value or substring is each index in the list
#syntax:variable_name.extend(itterable)


so=["python is a"]
print(so.extend("python"))
print(so)
any=[1,2,3]
print(any.append(6))
print(any)


#pop():used to remove the item from the list ,but will mention here index postion in the pop method
#syntax:variable_name.pop(index postion)

any=[1,2,3]
any.pop(0)
print(any)


'''
#remove:used to remove the item from the list,but will mention here direct in the remove method
#syntax:variable-name.remove(value)

any=[1,3,4]
any.remove(3)
print(any)
'''

      
      



        
