''' 
#1. pro to print Odd or Even

i=int(input("Enter a num "))
if i%2==0:
    print("Even num")
else:
    print("Odd num")
'''


'''
#Exercise 2: Positive or Negative

i=int(input("Enter a num "))
if i==0:
    print("The given num is Zero")
elif i>0:
    print("The given num is Positive")
elif i<0:
    print("The given num is Negative")
'''

'''
#Leap Year
     
i=int(input("Enter the Year "))
if i>=400:
    if i%400==0:
        print("The given year is Leap Year")
    else:
        print("The given year is not Leap Year")
if i<400:
    if i%4==0:
        print("The given year is Leap Year")
    else:
        print("The given year is not Leap Year")
'''        
     
''' #Exercise 4: Grade Calculator
     
i=float(input("Enter the Student Score "))

if i>100:
    print("Entered value is out of range")
        
elif i>=90:
    print("A")
        
elif i<60:
    print("D")
        
elif i>=80 and i<=89:
    print("B")
        
elif i>=70 and i<=79:
        print("C")
'''

'''
#Exercise 6: Vowel or Consonant

vowel=("a","e","i","o","u","A","E","I","O","U")

i=input("Enter a character: ")
if i in vowel:
#if (i=='A' or i=='a' or i=='E' or i =='e' or i=='I'
#or i=='i' or i=='O' or i=='o' or i=='U' or i=='u'):
    print(i,"Vowel")
else:
    print(i,"Consonant")
'''

#Exercise 5: Age Group   
'''
i=int(input("Enter the age"))
if i<=12:
    print("Child")
if i>=13 and i<=19:
    print("Teenager")
if i>=18 and i<=64:
    print("Adult")
if i>=65:
    print("Senior Citizen")
'''

#Exercise 7: Maximum of Three Numbers
'''
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: "))

if num1>num2 and num1>num3:
    print("the maximum number is ",num1)

elif num2>num1 and num2>num3:
    print("the maximum number is ",num2)
    
else:
    print("the maximum number is ",num3)
'''


#Exercise 8: Triangle Type
'''
a=int(input("Enter the length of triangle"))
b=int(input("Enter the length of triangle"))
c=int(input("Enter the length of triangle"))

if a==b and b==c:
    print("Triangle is Equilateral")
elif a==b or b==c or a==c:
    print("Triangle is Isosceles")
else:
    print("Triangle is Scalane")        
'''
    
#Exercise 9: Login system
'''
un=str(input("Enter User Name: "))
ps=str(input("Enter Password"))
if un=="admin" and ps=="password123: ":
    print("Login Successful.")
else:
    print("Login Failed.")
'''

#Exercise 10: Divisibility Check
'''
a=int(input("Enter a number"))
if a%3==0 and a%5==0:
    print("Divisible by both")
else:
    print("Not divisible by both")    
'''

'''
#Exercise 1: Print Numbers
for i in range(1,11):
    print(i)
'''

#Exercise 2: Sum of Numbers
'''
total=0
for i in range(1,101):
    total +=i
print("The sum of 1 to 100 is: ",total)
'''

#Exercise 3: Multiplication Table
'''
num=int(input("Enter a number"))
for i in range(1,11):
    print(num,"x",i,"=",num*i)
'''