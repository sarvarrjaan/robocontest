a = input()
print(len(a))
for i in a:
    n = ord(i)
    x = ''
    while n>=1:
        x += str(n%2)
        n = n//2
    print(x[::-1])