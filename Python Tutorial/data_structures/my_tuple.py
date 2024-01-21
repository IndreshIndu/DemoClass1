#1 Empty tuple can be created?
'''
a=()
print(a)
print(type(a))
'''


#2 tuple is heterogeneous?
'''
e=(1,2,"xyz", 1.2, 1-3j, True, None)
print(e)
print(e[0])
'''

#3 tuple can be modified? "NO"
'''
i=(123,"abc","xyz")  #cannot be modified by using "()" tuple
print(i)

i[2]="Indresh"       #index should be represented by "[]"
print(i)
'''

#4 can be print duplicate elements
'''
b=(1,2,3,4,5,5,6,7,8,9) 
print(b) 
'''

'''
b=(1,2,3,4,5,6,7,8,9,10) #slice method
#print(b)
print(b[0:4])
print(b[5:10])
#print(b[3:])
#print(b[:6])
#print(b[:])
#print(b[::2])
#print(b[-9:-2])
#print(b[-10:-5:2])
#print(b[::-1])
'''