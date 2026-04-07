# 260407

n, m = map(int, input().split())

cabinat = []
for idx in range(n):
    cabinat.append(idx+1)

for _ in range(m):
    i, j = map(int, input().split())
    cabinat[i-1:j] = cabinat[i-1:j][::-1]

print(*cabinat)