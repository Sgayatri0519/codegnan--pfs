#file handling:is an object of file to maintain serveral function of file like,creating,reading,updateing and deleteing the file.
#open a file:1.open()2.with open()
#there are modes:'r'is used to reading the file, error if file does not exit
#'a' is used to add the txt into file,if file does not exist
#'w' is used to add the txtx into file but it will override of all txt inside file.if the file does not exist it will create with that name
#'x' is used create the file but will through error if we are used 'r' mode to create
#example:
so=open('demo.txt',"r")
print(so.read())
so.close()

#program:
so=open('dm.txt','w')
print(so.write('nxt will be java'))
so.close()

#program:
with open('demo.txt','w') as so:
    print(so.write('java'))
#methods:write()read(): this method can read entrire file chunk by chunk where we can specify the side
#readline():can read only one line at a time in a file
with open('demo.txt', 'w') as any_:
    any_.write("hello")


#program
with open('demo.txt', 'r') as any_:
    print(any_.readline())

#program
with open("demo.txt", "r") as any_:
    print(any_.readlines())

#how to remove file
import os

os.remove("demo.txt")
print("File deleted successfully")    
