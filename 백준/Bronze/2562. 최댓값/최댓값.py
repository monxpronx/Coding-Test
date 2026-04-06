# 260406

num_list = []
for i in range(9):
    num_list.append(int(input()))

max = num_list[0]
max_i = 0
for i in range(9):
    if num_list[i] > max:
        max = num_list[i]
        max_i = i

print(max)
print(max_i+1)