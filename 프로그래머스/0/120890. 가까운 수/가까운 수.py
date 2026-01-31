# 260131

def solution(array, n):
    answer = 0
    min_loss = 101
    
    for num in array:
        if max(num,n) - min(num,n) < min_loss:
            min_loss = max(num,n) - min(num,n)
            answer = num
        elif max(num,n) - min(num,n) == min_loss:
            answer = min(answer, num)
            
    return answer