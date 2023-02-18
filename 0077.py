import math
x, y = map(float, input().split())
n = math.ceil((100-x)/(x-3*y))
print(n + 1)