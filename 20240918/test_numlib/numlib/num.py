def is_odd(n):
    return n%2==1
def is_even(n):
    return n%2==0
import math
def is_prime(n):
    n_sqrt=int(math.sqrt(n))
    for i in range(2,n_sqrt+1):
        if n%i==0:
            return False
    return True