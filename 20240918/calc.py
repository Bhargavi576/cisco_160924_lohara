""" def find_diff(first:int=1,second:int=0):
    return first-second

print(find_diff(20,10))
print(find_diff(second=10,first=20))
print(find_diff(second=10))
print(find_diff())


def change_name(names,index,name):
    names[index]=name
names=['rahul','modi']
print(names)
change_name(names,1,'modiji')
print(names)



#iterator protocol
print(sum([10,20,30])) """

""" def find_sum(first,second,*others):
    s=first+second
    if(len(others)>0):
        for num in others:
            s+=num
    print(type(others))
    return s

print(find_sum(10,20))
print(find_sum(10,20,30))
print(find_sum(10,20,30,40,50)) """



""" def find_sum(first,second,**others):
    s=first+second
    if(len(others)>0):
        for key in others:
            s+=others[key]
    print(type(others))
    return s

print(find_sum(first=10,second=20))
print(find_sum(first=10,second=20,third=30))
print(find_sum(first=10,second=20,third=30,fourth=40,fifth=50)) """



""" def fact(n):
    if n<=1:#base/edge case
        return 1
    return n*fact(n-1)

print(fact(5)) """

import math
def is_prime(n):
    n_sqrt=int(math.sqrt(n))
    for i in range(2,n_sqrt+1):
        if n%i==0:
            return False
    return True

#print(is_prime(5))
num=int(input())
print(is_prime(num))

