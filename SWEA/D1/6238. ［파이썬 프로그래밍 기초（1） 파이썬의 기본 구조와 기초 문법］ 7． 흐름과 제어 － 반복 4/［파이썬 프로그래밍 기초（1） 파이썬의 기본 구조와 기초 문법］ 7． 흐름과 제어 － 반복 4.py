# 260628

temp = ""
for i in range(1, 101):
    if i % 2 == 1:
        temp += str(i)
        temp += ", "

print(temp[:len(temp)-2])