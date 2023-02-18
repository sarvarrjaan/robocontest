n = int(input())
l = list(map(int, input().split()))
j = [i for i in l if i%2==0]
if j:
    print(max(j))
else:
    print(-1)