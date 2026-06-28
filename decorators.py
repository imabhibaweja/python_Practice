# #decorator is a function that takes a function, its creat a new function inside its body and then its return the new function.
# def dec(func):
#     def wrap():
#         print("Aman")
#         func()
#         print("Amisha")
#     return wrap

# def weds():
#     print("Weds")

# f = dec(weds)
# f()
# def repeat(n):
#     def decorator(func):
#         def wrapper(a):
#             for i in range(n):
#                 func(a)
#         return wrapper
#     return decorator

# @repeat(3)
# def greet(name):
#     print(f"Hello, {name}!")

# greet("world")
def uppercase(func):
    def wrapper():
        return func().upper()
    return wrapper
def name(func):
    def wrapper():
        return "Hello "+func()
    return wrapper

@uppercase
@name
def abhi():
    return "ABhi"

print(abhi())