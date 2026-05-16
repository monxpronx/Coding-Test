# 260516

T = int(input())

for t in range(1, T+1):

    N, K = map(int, input().split())
    total_list = []

    for n in range(1, N+1):

        mid_gr, final_gr, work_gr = map(int, input().split())
        total = (0.35 * mid_gr) + (0.45 * final_gr) + (0.2 * work_gr)
        total_list.append(total)

        if n == K:
            k_total = total

    total_list.sort(reverse=True)

    k_rank = 0
    for i in range(N):
        if total_list[i] == k_total:
            k_rank = i+1
            break

    grade = ''
    unit = N//10
    if k_rank <= unit:
        grade = 'A+'
    elif k_rank <= unit*2:
        grade = 'A0'
    elif k_rank <= unit*3:
        grade = 'A-'
    elif k_rank <= unit*4:
        grade = 'B+'
    elif k_rank <= unit*5:
        grade = 'B0'
    elif k_rank <= unit*6:
        grade = 'B-'
    elif k_rank <= unit*7:
        grade = 'C+'
    elif k_rank <= unit*8:
        grade = 'C0'
    elif k_rank <= unit*9:
        grade = 'C-'
    else:
        grade = 'D+'

    print("#{}".format(t), grade)