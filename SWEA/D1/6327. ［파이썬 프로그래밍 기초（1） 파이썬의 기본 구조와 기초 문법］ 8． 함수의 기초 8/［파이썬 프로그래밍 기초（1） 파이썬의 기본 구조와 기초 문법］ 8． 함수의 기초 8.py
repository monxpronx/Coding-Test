# 260622

tmp = input().split(',')

num_list = []
num_list.append(int(tmp[0]))
for i in range(1, len(tmp)):
    num_list.append(int(tmp[i][1]))

for num in num_list:
    print("square({}) => {}".format(num, num*num))