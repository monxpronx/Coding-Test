# 260211

def solution(array):
    answer = 0
    
    for num in array:
        num = str(num)
        for ch in num:
            if ch=='7':
                answer+=1
    
    return answer