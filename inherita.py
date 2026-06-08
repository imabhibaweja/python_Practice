class Animal: #parent class (superclass)
    def __init__(self, name):
        self.name = name
        print(self.name)
    
    def speak(self):
        print("Generic sound is.......")

class Dog(Animal): # child class
    def speak(self):
        print("Woof!!!!!")
    
class Cat(Animal): #child class
    def speak(self):
        print("Meaw!!!")

my_dog = Dog("Bruno")
my_cat = Cat("Kitty")
my_dog.speak()
my_cat.speak()
