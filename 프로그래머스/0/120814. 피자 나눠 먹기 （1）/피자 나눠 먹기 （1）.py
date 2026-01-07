# 260107

def solution(n):
    answer = 0
    
    while 1:
        if 7*answer >= n:
            break
        answer+=1
    
    return answer