n = int(input())
a = []
for i in range(n):
    x = int(input())
    k = bin(x).count('1')
    a.append(k)
for i in a:
    print(i)