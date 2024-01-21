'''
In Dictionary elements are stored in the form of Key-Value pair

'''

a={1:"Indresh",2:"Leander",3:"Nandini",4:"Soundarya"}
b=[1,2,3,4,5]
'''
print(a)
print(a[4])
a[1]="Indresh Indu"
a[4]="Soundarya N"
print(a)
c=a.fromkeys(b, None)
print(a)
print(c)
print(a.keys())
print(a.values())
a.clear()
a.pop(4)
a.remove(3)
'''

for i in range (2,3):
    b.pop(i)
print(b)