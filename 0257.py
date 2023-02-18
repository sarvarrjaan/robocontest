s = input()
l = s.split('0')
if s.count('1') == len(max(l)):
    print('YES')
else:
    print('NO')