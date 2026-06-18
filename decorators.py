#decorator is a function that takes a function, its creat a new function inside its body and then its return the new function.
def dec(func):
    def wrap():
        print("Aman")
        func()
        print("Amisha")
    return wrap

def weds():
    print("Weds")

f = dec(weds)
f()