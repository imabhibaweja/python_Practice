
class Employee:
    # def __init__ (self, name = "Unknown", post = "programmer", salary = 20000):
    #     self.name = name
    #     self.post = post
    #     self.salary = salary
    def __init__(self, name, post, salary):
        self.name = name
        self.post = post
        self.salary = salary

    # withot default values
    # def get_name(self):
    #     self.name = input("Enter name")
    #     return self.name

    # WITH DEFAULT VALUES
    def get_name(self):
        return self.name

    # withot default values

    # def get_salary(self):
    #     self.salary = input("Enter salary")
    #     return self.salary
    
    #WITH DEFAULT VALUES
    def get_salary(self):
        return self.salary

    #WITHOUT DEFAULT VALUES

    # def get_post(self):
    #     self.post = input("Enter Post")
    #     return self.post

    #WITH DEFAULT VALUES

    def get_post(self):
        return self.post
    
a = Employee("Abhi", "CEO", 50000) # without default values
b = Employee("Aman", "Director", 70000)
# c = Employee() # with default values
print(a.get_name())
print(a.get_post())
print(a.get_salary())
print()
print(b.get_name())
print(b.get_post())
print(b.get_salary())
print()
# print(c.get_name())
# print(c.get_post())
# print(c.get_salary())
    

# a=Employee()
# a_name = a.get_name()
# a_salary = a.get_salary()
# print(a_name)
# print(a_salary)