a = list(map(int, input().split()))
s = int(input())
print(max(0, s-sum(a)))