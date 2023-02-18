n = int(input())
a = []
for i in range(n):
    x = int(input())
    a.append(x**3 + x)
for i in a:
    print(i)