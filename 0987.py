import math
a,b=map(int,input().split())
c=math.factorial(a) if a<b else math.factorial(b)
print(c)