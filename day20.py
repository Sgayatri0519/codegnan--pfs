#error handling
#try block: the try block,test a block of code for error
#except block:the except block let hand if the code contain errors
try:
    print(10/0)
except:
    print('this will handle ZeroDivisionError')
#else:this will be excute,if the try block has no error in the code
try:
    print("any")
except NameError:    
    print('this will handle NameError')
else:
    print("No error")
#example
try:
    print(5+"py")
except NameError:    
    print('this will handle NameError')
#note:
try:
    print(a)
    print(2+"hai")
except TypeError:
    print("this will handle TypeError")
except NameError: 
    print("this will handle NameError")
#finaly block:this will be excuted either try block contain error or not
try:
    print(a)
except:
    print("error")
else:
    print("no error")
finally:
    print("end")
          

    
   
    
    
    
    
    
