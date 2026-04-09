# 260409

t = int(input())

for i in range(t):
    tmp = ""
    r, s = input().split()
    r = int(r)
    for ch in s:
        tmp += (ch * r)
    print(tmp)