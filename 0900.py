t=int(input())
s=1
for i in range(t):
  k,q,n=map(int,input().split())
  for i in range(n):
    q=(q+k)*2
  print(q)