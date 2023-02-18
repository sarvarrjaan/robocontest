n = int(input())
a = list(map(int, input().split()))
left = [i for i in a if i<0]
right = [i for i in a if i>0]
left, right = abs(sum(left)), abs(sum(right))
print(abs(left-right))