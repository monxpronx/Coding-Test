# 260514

T = int(input())

for i in range(1, T+1):

    n = int(input())
    num_list = list(map(int, input().split()))
    num_list.sort()
    print("#{}".format(i), *num_list)