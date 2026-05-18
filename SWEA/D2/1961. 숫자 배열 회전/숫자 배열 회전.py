# 260518

T = int(input())

for t in range(1, T+1):

    N = int(input())

    matrix = []
    for _ in range(N):
        tmp = list(map(int, input().split()))
        matrix.append(tmp)


    str_list = [""] * N

    # 90도 회전 행렬
    new_idx = 0
    for j in range(N):
        string = ""
        for i in range(N-1, -1, -1):
            string += str(matrix[i][j])
        str_list[new_idx] += string
        str_list[new_idx] += " "
        new_idx += 1

    # 180도 회전 행렬
    new_idx = 0
    for i in range(N-1, -1, -1):
        string = ""
        for j in range(N-1, -1, -1):
            string += str(matrix[i][j])
        str_list[new_idx] += string
        str_list[new_idx] += " "
        new_idx += 1

    # 270도 회전 행렬
    new_idx = 0
    for j in range(N-1, -1, -1):
        string = ""
        for i in range(N):
            string += str(matrix[i][j])
        str_list[new_idx] += string
        new_idx += 1

    # 출력
    print("#{}".format(t))
    for n in range(N):
        print(str_list[n])