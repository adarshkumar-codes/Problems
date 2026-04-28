# Task 1: Inheritance (The Foundation)
# Create a base class called Vehicle.

# Attributes: brand, model, and base_fare.

# Method: describe(), which returns a string like "This is a [brand] [model]."

# The Goal: Create two child classes: Taxi and Bus. Taxi should have an extra attribute for luxury_rating, and Bus should have passenger_capacity.

class Vehicle:
    brand = "",
    model = "",
    base_fare = 0.0

    def __init__(self, brand, model, base_fare):
        self.brand = brand
        self.model = model
        self.base_fare = base_fare

    def describe(self):
        return f'This is a {self.brand} {self.model}'
    
class Taxi(Vehicle):
    luxary_rating = 0
    def __init__(self, brand, model, base_fare,luxary_rating):
        super().__init__(brand, model, base_fare)
        self.luxary_rating = luxary_rating

class Bus(Vehicle):
    passenger_capacity = 0
    def __init__(self, brand, model, base_fare, passenger_capacity):
        super().__init__(brand, model, base_fare)
        self.passenger_capacity = passenger_capacity

Ola = Taxi('Supra','X1', 201, 5)
print(Ola.describe())

Volvo = Bus('IntrCity','Sleeper', 2000, 30)
print(Volvo.describe())



# Task 2: Encapsulation (Data Security)
# In your Vehicle class, make the base_fare a private attribute.

# The Goal: Create a @property (getter) to see the fare and a @setter to change it.

# The Constraint: The setter should check that the new fare is never lower than $5.00. If it is, print an error message instead of updating it.

class Vehicle:
    brand = "",
    model = "",
    __base_fare = 2.0

    @property
    def base_fare(self):
        return self.__base_fare
    
    @base_fare.setter
    def base_fare(self, base_fare):
        if base_fare > 5.0:
            self.__base_fare = base_fare
        else:
            print("Too low fare!")

C = Vehicle()
C.base_fare = 50.0
print(C.base_fare)



# Task 3: Abstraction (The Rulebook)
# Import ABC and abstractmethod. Make your Vehicle class an Abstract Base Class.

# The Goal: Define an abstract method called calculate_trip_cost(distance).

# The Constraint: Now, your Taxi and Bus classes must implement this method.

# Taxi might calculate it as distance * 2 + base_fare.

# Bus might just return the base_fare regardless of distance.

from abc import ABC, abstractmethod
class Vehicle(ABC):
    brand = "",
    model = "",
    base_fare = 0.0

    def __init__(self, brand, model, base_fare):
        self.brand = brand
        self.model = model
        self.base_fare = base_fare

    @abstractmethod
    def calculate_trip_cost(self, distance):
        pass

class Taxi(Vehicle):
    def __init__(self, brand, model, base_fare):
        super().__init__(brand, model, base_fare)

    def calculate_trip_cost(self, distance):
        return distance*2+self.base_fare

class Bus(Vehicle):
    
    def __init__(self, brand, model, base_fare):
        super().__init__(brand, model, base_fare)

    def calculate_trip_cost(self):
        return self.base_fare

Ola = Taxi('BMW','X4',230)
Volvo = Bus('Bus_name',"Bus_model", 40)
print(Ola.calculate_trip_cost(123))
print(Volvo.calculate_trip_cost())



# Task 4: Polymorphism (The System in Motion)
# Create a function (outside of any class) called start_transit_service(vehicle_list, distance).

# The Goal: This function should take a list containing both Taxi and Bus objects.

# The Action: Loop through the list and, for each vehicle, call .calculate_trip_cost(distance) and print the result.

# Why it works: The function doesn't need to know if it's looking at a bus or a taxi; it just trusts that every vehicle knows how to calculate its own cost.

class Vehicle():
    brand = "",
    model = "",
    base_fare = 0.0

    def __init__(self, brand, model, base_fare):
        self.brand = brand
        self.model = model
        self.base_fare = base_fare

    def calculate_trip_cost(self, distance):
        pass

class Taxi(Vehicle):
    def __init__(self, brand, model, base_fare):
        super().__init__(brand, model, base_fare)

    def calculate_trip_cost(self, distance):
        return distance*2+self.base_fare

class Bus(Vehicle):
    
    def __init__(self, brand, model, base_fare):
        super().__init__(brand, model, base_fare)

    def calculate_trip_cost(self,distance):
        return self.base_fare

def start_transit_service(vehicle_list, distance):
    for vehicle in vehicle_list:
        total = vehicle.calculate_trip_cost(distance)
        print(vehicle.brand,"costs",total)

A = Taxi('A', 'aaa', 200)
B = Bus('B', 'bbb', 40)
C = Taxi('C','aaa', 190)
start_transit_service([A,B,C], 300)


