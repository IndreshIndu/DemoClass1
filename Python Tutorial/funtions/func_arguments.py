'''
Arguments:

Category 1: Formal Arguments

a. default arguments
b. variables arguments
c. keyword variable arguments

category 2: Actual arguments
a. Positional arguments
b. keyword arguments
'''
from funtions.function_intro import add_mul
def add(a=0,b=0): #formal arguments, default arguments
    c=a+b
    print(c)
    
add(4, 5)     #actual arguments (based on passing actual arguments to the formal arguments)
add(b=5, a=3) #keyword argument 

def addition(*a):  #variable length argument - only accepts positional arguments(value)
    print(a)

addition(1,2)

def save(**a):  #Key variable length arguments
    print(a)

save(naame="abc",roll_no=1)

add_mul(1,4)

addition(1,2,3,4)
addition(1+2+3+4)