class Employee:
    # without default values
    def __init__(self, name, post, salary):
        self.name = name
        self.post = post
        self.salary = salary
    
    def get_name(self):
        return self.name

    def get_post(self):
        return self.post
    
    def get_salary(self):
        return self.salary
    
Abhi = Employee("Abhi", "CEO", 50000)
print(Abhi.get_name())
print(Abhi.get_post())
print(Abhi.get_salary())