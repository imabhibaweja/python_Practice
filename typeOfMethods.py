# class Animal:
#     species = "Mammal"  # Class attribute

#     @classmethod
#     def set_species(cls, new_species):
#         cls.species = new_species  # Modifies class attribute

#     @classmethod
#     def get_species(cls):
#         return cls.species

# print(Animal.get_species())  # Mammal
# Animal.set_species("Reptile")
# print(Animal.get_species())  # Reptile

# # You can also call class methods on instances, but it's less common:
# a = Animal()
# print(a.get_species()) # Reptile
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def from_string(cls, data):
#         name, age = data.split("-")
#         return cls(name, int(age))  # Creates a new Person instance

# p = Person.from_string("Alice-30")
# print(p.name, p.age)  # Alice 30

class Math4U:
    @staticmethod
    def add(a, b):
        return a + b

print(Math4U.add(3, 5))  # 8

#Can also be called on an instance
m = Math4U()
print(m.add(4,5)) # 9