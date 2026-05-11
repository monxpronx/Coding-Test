# 260511

N = int(input())

temp = []
for i in range(1, N+1):
    if N%i==0:
        temp.append(i)

print(*temp)