n = int(input())
d = [0]*n
for i in range(n):
  d[i] = list(map(int, input().split()))
for i in range(n):
  x = d[i][2] - d[i][0]
  y = d[i][3] - d[i][1]
  print(d[i][2] +  x,d[i][3] + y)