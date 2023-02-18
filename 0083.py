s, t = map(int, input().split())
a, b = map(int, input().split())
m, n = map(int, input().split())
m = list(map(int, input().split()))
n = list(map(int, input().split()))
a = [i for i in m if i>0 and i+a>=s and i+a<=t]
b = [i for i in n if i<0 and i+b<=t and i+b>=s]
print(len(a))
print(len(b))