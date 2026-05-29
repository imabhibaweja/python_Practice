a=(10,20)
print(a, type(a))
b=list(a)
print(b, type(b))
b[0]=50
a=tuple(b)
print(a, type(a))