"""
robocontest.uz #yolg'iz_son

instagram.com/sarvarrjaan   #follow_me
"""

n = int(input())
a = list(map(int, input().split()))
for i in a:
    if a.count(i) == 1:
        print(i)
        break
