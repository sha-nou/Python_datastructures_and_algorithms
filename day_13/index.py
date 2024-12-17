#classes
class Dog:
    species='Leo panthera'
    def __init__(self,name,age):
        self.name =name
        self.age = age
    def __str__(self):
        return f"{self.name} is  {self.age } old" 
    
    def speak(self,sound):
        return f"{self.name} says {sound}"

class Bulldog(Dog):
    pass

class Caniche(Dog):
    pass


class GoldenRetriever(Dog):
    def speak (self,sound='Bark'):
        return super().speak(sound)

miles = Bulldog("Miles",4)
buddy = Caniche("Buddy", 9)
rufus = GoldenRetriever("rufus",5)

print(rufus.speak())
print(miles.species)
print(type(miles))

# class Car:
#     def __init__(self,color,mileage):
#         self.color=color
#         self.mileage=mileage
#     def __str__(self):
#         return f"A {self.color} car which runs at {self.mileage} miles everyday"

# myCar=Car('Brown',250)
# newCar =Car('Red',20000)
# print(myCar,newCar)

# for car in(myCar,newCar):
#     print(car)

# class Parent:
#     speaks='English'
    
# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self.speaks.append("Lingala")
# print(Child)