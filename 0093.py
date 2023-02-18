def tak(s):
    a = [s[i] for i in range(len(s))]
    a.sort()
    x = [a[0]]
    for i in range(len(a)-1):
        if a[i] != a[i+1]:
            x.append(a[i+1])
    return len(x)
n = int(input())
x = []
for i in range(n):
    x.append(input())
for i in x:
    print(len(i)-tak(i))