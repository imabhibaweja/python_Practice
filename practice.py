# a=(10,20)
# print(a, type(a))
# b=list(a)
# print(b, type(b))
# b[0]=50
# a=tuple(b)
# print(a, type(a))
numbers = {"Abhi":7410841001, "Rohit":7410841002, "Satyarth":7410841003}
print(numbers.keys())
print(numbers.values())
for keys, values in numbers.items():
    print(keys, values)