# 260510

n = int(input())
tmp = []

for i in range(n, -1, -1):
    tmp.append(i)

print(*tmp)