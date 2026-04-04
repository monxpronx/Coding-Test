# 260404

total = int(input())

if total % 4 == 0:
    cnt_4 = total//4
else:
    cnt_4 = total//4 + 1

string = "int"
for i in range(cnt_4):
    string = "long " + string

print(string)