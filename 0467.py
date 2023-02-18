n, m = map(int, input().split())
if m%2 == 1:
    print(-1)
else:
    print(n + m//2 + 1)