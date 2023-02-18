a,s=map(int,input().split(':'))
n=int(input())
mn=a*60+s+n
h=mn//60
m=mn%60
hour=h%24
hr=hour if hour>=10 else "0" + str(hour)
minut=m if m>=10 else "0" + str(m)
print(f'{hr}:{minut}')