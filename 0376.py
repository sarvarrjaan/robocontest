N=int(input())
if N>12:
  print("Error")
elif N<3 or N>11:
  print("Winter")
elif N<6:
  print("Spring")
elif N<9:
  print("Summer")
else:
  print("Autumn")