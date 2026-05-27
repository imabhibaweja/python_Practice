def fact(a):
    if(a==0 or a==1):
        return 1
    return a*fact(a-1)
def fibbo(a):
    if(a==0 or a==1):
        return a
    return fibbo(a-1)+fibbo(a-2)
print(fact(5))
print(fibbo(5))
print(fibbo(6))