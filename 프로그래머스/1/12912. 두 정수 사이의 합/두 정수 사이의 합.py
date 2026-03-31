# 260331

def solution(a, b):
    answer = 0
    
    min_num = min(a,b)
    max_num = max(a,b)
    
    for n in range(min_num, max_num+1):
        answer+=n
    
    return answer