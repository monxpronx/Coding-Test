# 260519

N = int(input())
answer = ""

for n in range(1, N+1):

    str_n = str(n)

    # 일단 369 개수 카운트
    cnt = 0
    for ch in str_n:
        if ch == '3' or ch == '6' or ch =='9':
            cnt += 1
    
    if cnt == 0:
        answer += str_n
    else:
        answer += ("-" * cnt)

    answer += " "

print(answer)