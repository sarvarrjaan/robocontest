a, b = map(float, input().split())
a, b = (a+b)/2 , (a*b)**0.5
if a > b:
    print('>')
elif a < b:
    print('<')
elif a == b:
    print('=')
else:
    print('<')