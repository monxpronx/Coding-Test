# 260511

n = int(input())

tmp = 1
temp = [1]
for _ in range(n):
    temp.append(tmp*2)
    tmp *= 2

print(*temp)