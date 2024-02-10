'''
Exception: which is not normal/ abnormal

Errors:
1. syntax errors: These are completely under programmer's control
2. Run-time errors: Unexpected
 
'''

#a=float(input("Enter a number: "))
#print(a)
#print("Program terminated")

print(1+2)
print(2*3)

try:
    try:
        print(10/0)
#except:
#    print("Invalid input")

#except ZeroDivisionError as ze: #individual handling of each errors #specific error
#    print("Zero Division Error")
#    print(ze)
    
#except TypeError as te:
#    print("Type error")
#    print(te)

    except (ZeroDivisionError, TypeError) as msg: #handling multiple exception in one block
        print("Error message:",msg)
    
        print(3/"abc")
    
except Exception as msg: #default exception block
    print(msg)

print(5%2)
print(23/2)


