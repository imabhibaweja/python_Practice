
class Employee:
    def __init__ (self, name = "Unknown", post = "programmer", salary = 20000):
        self.name = name
        self.post = post
        self.salary = salary

    def get_name(self):
        return self.name
    
    def get_salary(self):
        return self.salary
    
    def get_post(self):
        return self.post
    
a = Employee("Abhi", "CEO", 50000)
b = Employee("Aman", "Director", 70000)
c = Employee("Harshita")
print(a.get_name())
print(a.get_post())
print(a.get_salary())
print()
print(b.get_name())
print(b.get_post())
print(b.get_salary())
print()
print(c.get_name())
print(c.get_post())
print(c.get_salary())
    

# a=Employee()
# a_name = a.get_name()
# a_salary = a.get_salary()
# print(a_name)
# print(a_salary)