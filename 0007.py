"""
robocontest.uz #Bayroq

instagram.com/sarvarrjaan   #follow_me
"""

n = int(input())
a = [2, 2]
for i in range(2,46):
    a.append(a[i-1] + a[i-2])
print(a[n-1])
