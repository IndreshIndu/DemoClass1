'''
list
1. Empty list can be created?
2. List is heterogeneous- list can be created with different data type elements
3. List can be modified?
4. List can be created with duplicate elements?
'''

'''
#1
a=[]
print(a)
print(type(a))
'''

#2
'''
b=[1,2,3,4]
c=list(range(1, 5))
print(c)
d=["abc", "xyz"]

e=[1,2,"xyz", 1.2, 1-3j, True, None]
print(e)
print(b[0])  # accessing individual elements using indexing
'''

'''
b=[1,2,3,4,5,6,7,8,9]
for i in b:    # accessing individual elements using for loop
    if i%2==0:
        print(i)
'''

'''
#3

e=[1,2,"xyz", 1.2, 1-3j, True, None]
print(e)

e[2]="Indresh" #by modifying / replacing
print(e)
'''

'''
b=[1,2,3,4,5,6,7,8,9,10] #slice method
#print(b)
#print(b[0:4])
#print(b[5:10])
#print(b[3:])
#print(b[:6])
#print(b[:])
#print(b[::2])
#print(b[-9:-2])
#print(b[-10:-5:2])
#print(b[::-1])
'''

#4
'''
b=[1,2,3,4,5,5,6,7,8,9] #can be print duplicate elements
print(b)     
'''   

b=[1,2,3,4,5,6,7,8,9,10]
b.append(23)
b.append([2,3,4])
print(b)
      
print(len(b))    #comes under tople function    

b.reverse()  #reverse the op
print(b)      

f=["abc","eft","bsd","ght"]
f.sort()
print(f)
f.sort(reverse=True)
print(f)        