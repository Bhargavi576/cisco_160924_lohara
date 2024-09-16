def fact(n):
    fact=1
    for i in range(n,1,-1):
        fact=fact*i
    return fact

f1 =fact(5)
f2 =fact(4)
print(f1)
print(f2)
