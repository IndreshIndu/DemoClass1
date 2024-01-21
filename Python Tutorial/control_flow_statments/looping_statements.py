'''
1. while loop
2. for loop

1. while loop statement:
a. Initialization 
b. condition Expression
c. increment / decrement

'''

'''(
position=1
while position<=10:
    print(position)
    #position=position+1
    position +=1'''
    
num=int(input("Enter the num from 1-101: "))         
for i in range (1,101):
    
    if i==num:
        continue
    
    if i % 2==0:
        print(i)
        
    #if i==num:
     #   break