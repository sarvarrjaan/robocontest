n = int(input())
m = list(map(int, input().split()))
m.sort()
a = [m[0]]
for i in range(len(m)-1):
    if m[i] != m[i+1]:
        a.append(m[i+1])
a = [[m.count(i),i] for i in a]
a.sort()
for i in a:
    if i[0] == a[-1][0]:
        print(i[1])
        break