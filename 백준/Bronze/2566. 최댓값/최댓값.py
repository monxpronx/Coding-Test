# 260412

arr = []

for i in range(9):
    arr.append(list(map(int, input().split())))

max_value = arr[0][0]
max_i, max_j = 1, 1
for i in range(9):
    for j in range(9):
        if arr[i][j] > max_value:
            max_value = arr[i][j]
            max_i = i
            max_j = j

print(max_value)
print(max_i+1, max_j+1)