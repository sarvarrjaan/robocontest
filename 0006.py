"""
robocontest.uz #Dasturchilar kuni

instagram.com/sarvarrjaan   #follow_me
"""

year = int(input())
years = str('0'*(4-len(str(year))))+str(year)
if year%400 == 0 or (year%4 == 0 and year%100 != 0):
    print("12/09/"+years)
else:
    print("13/09/"+years)
