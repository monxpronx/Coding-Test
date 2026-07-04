# 260704

T = int(input())

for t in range(1, T+1):

    N = int(input())

    arr = []
    for _ in range(N):
        tmp = list(map(int, input().split()))
        arr.append(tmp)

    
    new_line = [""] * N

    # 90도 회전 모양
    for j in range(N):
        for i in range(N-1, -1, -1):
            new_line[j] += str(arr[i][j])

    for n in range(N):
        new_line[n] += " "

    # 180도 회전 모양
    for i in range(N-1, -1, -1):
        for j in range(N-1, -1, -1):
            new_line[N-i-1] += str(arr[i][j])

    for n in range(N):
        new_line[n] += " "

    # 270도 회전 모양
    for j in range(N-1, -1, -1):
        for i in range(N):
            new_line[N-j-1] += str(arr[i][j])

    
    print("#{}".format(t))
    for n in range(N):
        print(new_line[n])