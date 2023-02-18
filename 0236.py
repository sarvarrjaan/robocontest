n = int(input())

if n<0:
    print(-1 * (abs(n)*(abs(n)+1))//2 + 1)
else:
    print(n*(n+1)//2)