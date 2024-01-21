'''
Abstraction: 

Interface: define as a abstract class containing abstract methods only
           -> all interface are abstract class but all 
              abstraction are not interface. 
'''

from abc import ABC, abstractmethod

class Car(ABC):
    def no_of_wheels(self):
        print("Car has 4 wheels") #implemented method
    
    @abstractmethod
    def no_of_seats(self):  #unimplemented method
        pass
        
        
class SUV(Car):
    def no_of_seats(self):
        print("Car has 8 seats")
             
    def display_suv(self):
        print("This is SUV car")
        
duster=SUV()
duster.display_suv()
duster.no_of_seats()
        