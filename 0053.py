n = int(input())

if n == 1 or n == 2:
    print(0)
else:
    print(n*(n-3) // 2)