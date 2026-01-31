# 260131

def solution(order):
    answer = 0
    
    order = str(order)
    
    for ch in order:
        if ch in '369':
            answer += 1
    
    return answer