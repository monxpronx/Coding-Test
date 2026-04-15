# 260415

def solution(n):
    answer = 0

    str_n = str(n)
    for ch in str_n:
        answer += int(ch)
    
    return answer