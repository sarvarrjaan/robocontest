S = input()
S=S.lower()
for i in S:
  if 'a' in S:
    S=S.replace('a', '')
  elif 'o' in S:
    S=S.replace('o', '')
  elif 'u' in S:
    S=S.replace('u', '')
  elif 'i' in S:
    S=S.replace('i', '')
  elif 'e' in S:
    S=S.replace('e', '')
  elif 'y' in S:
    S=S.replace('y', '')
print('.'+'.'.join(S))