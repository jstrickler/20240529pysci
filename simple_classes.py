
# radio = schematic()
# house = blueprint()
# obj = class()  create an instance of a class 
colors = list()
cities = list() 
# obj.method(...)
colors.append("pink")
colors.insert(0, 'blue')
# print obj
print(f"{colors = }")

class Mammal:
    def run(self):
        print("running...")

class Dog(Mammal):
    def bark(self):
        print("Woof! Woof!")

d1 = Dog()
print(f"{type(colors) = }")

print(f"{type(d1) = }")

d1.bark()  # self is d1
# Dog.bark(d1) don't do this

d2 = Dog()
d2.bark()  # self is d2   

d1.run()
d2.run()