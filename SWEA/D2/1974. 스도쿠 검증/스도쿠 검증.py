# 260516

T = int(input())

for t in range(1, T+1):

    # 9x9 스토쿠 배열 입력
    stoku = []
    for _ in range(9):
        tmp = list(map(int, input().split()))
        stoku.append(tmp)

    flag = 1


    # 행 기준 검사
    for i in range(9):
        if len(set(stoku[i])) != 9:
            flag = 0
            break


    # 열 기준 검사
    for j in range(9):

        if flag==0:
            break

        tmp = []
        for i in range(9):
            tmp.append(stoku[i][j])
        if len(set(tmp)) != 9:
            flag = 0
            break


    # 사각형 검사
    for i in [0, 3, 6]:

        if flag==0:
            break

        for j in [0, 3, 6]:
            tmp = []
            for k in range(3):
                for l in range(3):
                    tmp.append(stoku[i+k][j+l])
            if len(set(tmp)) != 9:
                flag = 0
                break
        if flag == 0:
            break

    print("#{} {}".format(t, flag))