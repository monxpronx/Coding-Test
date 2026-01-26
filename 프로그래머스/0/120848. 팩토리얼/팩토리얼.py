# 260126

def solution(n):
    answer = 1
    fac = 1
    
    while fac*(answer+1) <= n:
        answer += 1
        fac *= answer
        
    return answer