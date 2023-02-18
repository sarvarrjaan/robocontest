x = []
for i in range(7):
    l = list(map(int, input().split()))
    x.append(l)
    for j in l:
        if j == 1:
            k = [i, l.index(1)]
print(sum([abs(i - 3) for i in k]))