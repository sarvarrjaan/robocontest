n = int(input())
if n>37:
    if n%5 < 3:
        print(n)
    else:
        print((n//5 + 1)*5)
else:
    print(n)