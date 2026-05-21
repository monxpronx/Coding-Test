# 260521

T = int(input())

for t in range(1, T+1):

    N, M = map(int, input().split())

    num_list = list(map(int, input().split()))

    def rotate(num_list):

        new_list = num_list[1:]
        new_list.append(num_list[0])
        return new_list
    
    for _ in range(M):
        num_list = rotate(num_list)

    print("#{} {}".format(t, num_list[0]))