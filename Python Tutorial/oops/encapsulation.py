'''
Encapsulation: Wrapping up of data and methods that work on data within one unit.

Access Modifiers:
1. Public
2. Protected:"_"  can be accessed only inside class and its sub classes
3. Private:"__"  can be access only inside the class
'''

class CarClass:
    
    company="abc"   
    
    def __init__(self, name, roll_no):  
        self._name=name   #Protected variables
        self.__roll_num=roll_no 
    def display_details(self):
        print(f"{self.name} car is created for {CarClass.company} company")
            
    def move_forward(self,speed):
        print(f"{self.name} Car moving forward at {speed} kmph")
        
car1=CarClass("abc",101)
print(car1._name)
print(car1._CarClass__roll_num) #Name mangling
print(dir(car1))