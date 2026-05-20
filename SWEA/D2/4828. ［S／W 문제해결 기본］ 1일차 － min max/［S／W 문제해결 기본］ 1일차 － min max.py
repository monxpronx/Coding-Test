# 260520

T = int(input())

for t in range(1, T+1):

    N = int(input())
    num_list = list(map(int, input().split()))
    print("#{} {}".format(t, max(num_list)-min(num_list)))