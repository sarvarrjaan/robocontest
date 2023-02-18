x1,y1,x2,y2 = map(int, input().split())

x = abs(x2-x1)
y = abs(y2-y1)

if max(x, y)%2 == 0:
    print(max(x, y)//2)
else:
    print(max(x, y) * 0.5)