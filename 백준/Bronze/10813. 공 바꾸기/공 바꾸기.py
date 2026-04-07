# 260407

n, m = map(int, input().split())

cabinat = []
for idx in range(n):
    cabinat.append(idx+1)

for _ in range(m):
    i, j = map(int, input().split())
    tmp = cabinat[i-1]
    cabinat[i-1] = cabinat[j-1]
    cabinat[j-1] = tmp

print(*cabinat)