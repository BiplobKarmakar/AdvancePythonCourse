'''1. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class.
Expected Output: Vehicle Name: School Volvo Speed: 180 Mileage: 12

'''

class Vehicle:
        
        def __init__(self, name,speed,mileage):
         
         self._name = name
         self._speed=speed
         self._mileage=mileage
                

        def get_name(self):
          return self._name
      
    # setter method
        
        def get_speed(self):
          return self._speed
      
    # setter method
       
        def get_mileage(self):
          return self._mileage
      
    # setter method
      
class Bus(Vehicle):
   
   
   def __init__(self,name,speed,mileage):
       super().__init__(name,speed,mileage)

       
bus=Bus('school volvo',180,12)

print(bus.get_name(),bus.get_speed(),bus.get_mileage())



