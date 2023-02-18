t = int(input())
x = []
for i in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    x.append(sum(a[m:]) - sum(a[:(n-m)]))
for i in x:
    print(i)