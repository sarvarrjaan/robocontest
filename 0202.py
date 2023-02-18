gugurt = {
    '0' : 6,
    '1' : 2,
    '2' : 5,
    '3' : 5,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 3,
    '8' : 7,
    '9' : 6
    }

n = int(input())
s = [gugurt.get(i) for i in str(n)]
print(sum(s))