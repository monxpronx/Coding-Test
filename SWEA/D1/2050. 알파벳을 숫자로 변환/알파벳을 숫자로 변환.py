# 260511

string = input()
temp = ""

for ch in string:
    num = ord(ch) - ord('A') + 1
    temp += str(num)
    temp += " "

print(temp)