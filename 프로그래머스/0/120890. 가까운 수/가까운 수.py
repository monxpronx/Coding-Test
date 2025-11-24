# 251124

def solution(array, n):
    answer = 0
    min_gap = float('inf')
    
    for num in array:
        
        if num>n:
            gap = num-n
        else:
            gap = n-num
        
        gap = abs(gap)
        
        if gap < min_gap:
            min_gap = gap
            answer = num
        elif gap == min_gap:
            answer = min(answer, num)
            
    
    return answer