# 260406

n, m = map(int, input().split())
cabinat = [0]*n

for _ in range(m):
    i, j, k = map(int, input().split())
    for idx in range(i-1,j):
        cabinat[idx] = k

tmp = ""
for idx in range(n):
    tmp += str(cabinat[idx])
    tmp += " "
print(tmp)