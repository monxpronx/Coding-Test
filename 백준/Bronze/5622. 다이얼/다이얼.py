# 260409

s = input()

t = 0
for ch in s:
    if ch in "ABC":
        t += 3
    elif ch in "DEF":
        t += 4
    elif ch in "GHI":
        t += 5
    elif ch in "JKL":
        t += 6
    elif ch in "MNO":
        t += 7
    elif ch in "PQRS":
        t += 8
    elif ch in "TUV":
        t += 9
    else:
        t += 10

print(t)