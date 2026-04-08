# 260408

s = input()
temp = ""

for ch in "abcdefghijklmnopqrstuvwxyz":
    tmp = s.find(ch)
    temp += str(tmp)
    temp += " "

print(temp)