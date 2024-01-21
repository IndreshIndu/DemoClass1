'''
Inheritance: acquiring the properties of ancestor classes 
1. Simple/single level inheritance
2. multiple level inheritance 
3. multilevel level inheritance
'''

class GrandFather:  #Base class
    def __init__(self,name,age): 
        self.name=name
        self.age=age       
        print(f"GF name is {name} and of age {age}")
        
    def gf_method(self):
        print("This is GF method")
        
        
class Father(GrandFather): #Derived class (from base class)
    def __init__(self,name,age,adhaar_id):
        super().__init__(name,age)
        #self.name=name
        #self.age=age
        self.adhaar_id=adhaar_id        
        print(f"Father name is {self.name} and of age {self.age} and adhaar id is {self.adhaar_id}")
    
    def f_method(self,):
        print("This is Father method")
    
    def car(self):
        print("This is Father's car")
        
        
class Mother:
    def m_method(self):
        print("This is Mother method")        
    
    def car(self):
        print("This is Mother's car")   
                 
        
        
class Child(Father, Mother): 
    
    def c_methor(self):
        print("This is child method")
    
    def car(self):
        print("This is my car")
        
obj1=GrandFather("Ajja",120)  #Simple/single level inheritance
#obj1.gf_method()

obj2=Father("Appa",60,123)       #multiple inheritance
#obj2.f_method()
#obj2.gf_method()

obj3=Child("Nanu",23,456)        #multilevel inheritance
#obj3.gf_method()
#obj3.f_method()
#obj3.c_methor()
#obj3.m_method()
#obj3.car()

#print(Child.mro())