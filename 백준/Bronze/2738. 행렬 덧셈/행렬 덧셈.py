# 260412

n, m = map(int, input().split())

arr1 = []
for i in range(n):
    arr1.append(list(map(int, input().split())))

arr2 = []
for i in range(n):
    arr2.append(list(map(int, input().split())))

arr3 = []
for i in range(n):
    arr3.append([])
    for j in range(m):
        arr3[i].append((arr1[i][j])+(arr2[i][j]))

for i in range(n):
    print(*arr3[i])