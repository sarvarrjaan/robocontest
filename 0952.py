n=int(input())
d=n*(n-1)*(n-2)
if n==1 or n==2:
  print(n)
else:
  print(d%1000000007)