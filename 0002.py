"""
robocontest.com #katta-kichik, #taqqoslash

instagram.com/sarvarrjaan
"""

A, B=input().split()
if int(A)>int(B):
  c=">"
elif int(A)==int(B):
  c="="
elif int(A)<int(B):
  c="<"
print(c)
