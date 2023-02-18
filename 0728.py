a,b=map(int,input().split())
for i in range(1,10000):
  d=b*i
  if d>=a:
    print(d)
    break