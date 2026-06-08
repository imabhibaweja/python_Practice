class Employee:
    post = "Programmer" #class attribute
    # without default values
    # def __init__(self, name, post, salary): # here post is instance attribute
    #     self.name = name
    #     self.post = post
    #     self.salary = salary

    def __init__(self, name, salary): # here post is instance attribute
        self.name = name
        self.salary = salary
    
    def get_name(self):
        return self.name

    
    def get_salary(self):
        return self.salary
    
# Abhi = Employee("Abhi", "CEO", 50000)
Harshita = Employee("Harshita", 10000)
print(Harshita.get_name())
print(Harshita.post)
print(Harshita.get_salary())