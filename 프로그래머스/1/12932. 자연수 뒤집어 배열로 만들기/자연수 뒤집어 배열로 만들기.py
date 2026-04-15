# 260415

def solution(n):
    answer = []
    
    str_n = str(n)
    rev_n = str_n[::-1]
    
    for ch in rev_n:
        answer.append(int(ch))
    
    return answer