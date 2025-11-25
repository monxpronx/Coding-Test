# 251125

def solution(numbers, k):
    answer = numbers[0]
    idx = 0
    
    while k > 1:
        
        if idx == len(numbers)-2:
            idx = 0
        elif idx == len(numbers)-1:
            idx = 1
        else:
            idx += 2
            
        answer = numbers[idx]
        k -= 1
    
    return answer