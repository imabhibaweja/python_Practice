# a=(10,20)
# print(a, type(a))
# b=list(a)
# print(b, type(b))
# b[0]=50
# a=tuple(b)
# print(a, type(a))
# numbers = {"Abhi":7410841001, "Rohit":7410841002, "Satyarth":7410841003}
# print(numbers.keys())
# print(numbers.values())
# for keys, values in numbers.items():
#     print(keys, values)
# a = [1, 2, 3, 2, 4, 1, 5, 1, 2, 3]
# print(a, type(a))
# b = set(a)  
# print(b, type(b))
# a=list(b)
# print(a, type(a))
rate = {"a": 20, "b": 90, "c": 60}
rate2 = {"d": 30, "e": 80, "b": 70}
rate |= rate2
print(rate)