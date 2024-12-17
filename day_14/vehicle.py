
class  Vehicle:
    def __init__(self,make,year,model,color):
        self.year=year
        self.model=model
        self.make=make
        self.color=color
    def display_info(self):
        return f"{self.year} {self.make} {self.model} in {self.color} color."

class Car(Vehicle):
    def __init__(self,make,year,model,color,num_of_doors):
        super().__init__(make,year,model,color)
        self.num_of_doors=num_of_doors
    def info(self):
        super().display_info()
        return f"It has {self.num_of_doors} doors"

class Truck(Vehicle):
    def __init__(self,make,year,model,color,payload_cap):
        super().__init__(make,year,model,color)
        self.payload_cap=payload_cap
    def info(self):
        super().display_info()
        return f"It can carry atmost {self.payload_cap} kg"


class Bicycle(Vehicle):
    def __init__(self,make,year,model,color,num_of_tyres):
        super().__init__(make,year,model,color)
        self.num_of_tyres=num_of_tyres
    
    def info(self):
        super().display_info()
        return f"It has {self.num_of_tyres} wheels"

class Bus(Vehicle):
    def __init__(self,make,year,model,color,num_of_seats):
        super().__init__(make,year,model,color)
        self.num_of_seats=num_of_seats
    def info(self):
        super().display_info()
        return f"It has {self.num_of_seats} seats"
        

carina=Car('Toyota',2000,'Carina','red',4)
print(carina.display_info())