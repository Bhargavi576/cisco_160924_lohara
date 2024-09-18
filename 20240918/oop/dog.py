class Dog:
    species = "Canis lupus familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def description(self):
        return f"{self.name} is {self.age} years old."
    def speak(self, sound):
        return f"{self.name} says {sound}."
dog1 = Dog("Buddy", 3)
print(dog1.description())  
print(dog1.speak("Woof!"))  

dog2=Dog("tannie",4)
print(dog2.description())
print(dog2.speak("BowBow"))

dogs=[dog1,dog2]
from functools import reduce
#reduce syntax
#reduce(<func>,iterable,init_values)
ages_sum=reduce((lambda s,dog: s+dog.age),dogs,0)
print(ages_sum)
