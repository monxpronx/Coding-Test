# 260406

n, x = map(int, input().split())
num_list = list(map(int, input().split()))

tmp = []
for i in range(n):
    if num_list[i] < x:
        tmp.append(num_list[i])

for i in range(len(tmp)):
    print(tmp[i])