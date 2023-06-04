'''2. Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is 
seating capacity * 100. If Vehicle is Bus instance, we need to add an extra 10% on full fare as a 
maintenance charge. So total fare for bus instance will become the final amount = total fare + 10% of 
the total fare.
'''

class Vehicle:
    def __init__(self,capacity):
        self.capacity=capacity
       # fullfare=capacity*100
    def getfare(self):
        fullfare=self.capacity*100
        return fullfare    

class Bus(Vehicle):
    def __init__(self,capacity):
        super().__init__(capacity)


Vehicle=Bus(20)
print('vehicle=' , Vehicle.getfare())
bus=Bus(50)

print(bus.getfare())

yes = isinstance(Vehicle, Bus)
print(yes)
if yes:
    finalamount = bus.getfare()+bus.getfare()*0.1
    print(finalamount)



