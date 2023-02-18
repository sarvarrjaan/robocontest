import math
def isprime(num):
    a=2
    while a<=math.sqrt(num):
        if num%a<1:
            return False
        a=a+1
    return True
n = int(input())
if n == 3:
    print(2)
else:
    if isprime(n+1):
        print(n)
    else:
        print(0)