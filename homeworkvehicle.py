'''1. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class.
Expected Output: Vehicle Name: School Volvo Speed: 180 Mileage: 12

'''

class Vehicle:
       
     
       def get_name(self):
          return self._name
      
    # setter method
       def set_name(self, name):
           self._name = name

       def get_speed(self):
          return self._speed
      
    # setter method
       def set_speed(self, speed):
           self._speed = speed
 
       def get_mileage(self):
          return self._mileage
      
    # setter method
       def set_mileage(self, mileage):
           self._mileage = mileage
 
    

class Bus(Vehicle):
   pass
   
 
bus=Bus()
bus.set_name('school volvo')
bus.set_speed(180)
bus.set_mileage(12)

print(bus.get_name(),bus.get_speed(),bus.get_mileage())



