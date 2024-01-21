'''


'''
class CarClass:
    
    company="abc"   #class variable(it will not change with method or object variables it's constant
    
    def __init__(self, name):  #method variable
        self.name=name   #instance / object variable
        
    def display_details(self): #By using the “self” we can access the attributes and methods of the class in Python.
        print(f"{self.name} car is created for {CarClass.company} company")
            
    def move_forward(self,speed):
        print(f"{self.name} Car moving forward at {speed} kmph")
    def move_backward(self):
        print(f"{self.name} Car moving backward")
        
swift=CarClass("swift") #To call Class
duster=CarClass("duster")
#print(type(swift))
#print(type(duster))
#print(id(swift))
#print(id(duster))
#print(swift is duster)

swift.move_forward(50)  #To call method
duster.move_forward(100)
swift.move_backward()
duster.move_backward()
swift.display_details()
duster.display_details()

print(swift.name)
print(duster.name)