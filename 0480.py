a, b = map(int, input().split())
if b%100 + b == 1932:
    print(2022-a, 2022-b)
else:
    print('NO')