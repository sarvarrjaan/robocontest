"""
robocontest.uz #Kanfetlar
instagram.com/sarvarrjaan   #follow_me
"""

import math
t=int(input())
for i in range(t):
  n,k=map(int,input().split())
  v=math.factorial(n+k-1)/(math.factorial(n-1)*math.factorial(k))
  print(int(v))
