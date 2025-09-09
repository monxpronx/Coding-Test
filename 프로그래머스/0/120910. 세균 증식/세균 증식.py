# 250909

def solution(n, t):
    answer = 0
    
    answer = n  # 처음 세균
    for i in range(t):
        answer *= 2
    
    return answer