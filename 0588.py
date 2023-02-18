n=int(input())
X=0
for i in range(n):
  x=input()
  if x[0]=='+' or x[2]=='+':
    X=X+1
  else:
    X=X-1
print(X)