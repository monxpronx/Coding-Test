# 260408

t = int(input())
for i in range(t):
    s = input()
    tmp = "".join(s[0]+s[len(s)-1])
    print(tmp)