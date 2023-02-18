n = int(input())
k = n//10 * 2
a = n%10
if 3 in range(n%10 + 1):
    k += 1
if 7 in range(n%10 + 1):
    k += 1
print(k)