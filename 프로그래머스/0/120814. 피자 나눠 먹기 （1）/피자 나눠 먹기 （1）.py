# 251119

def solution(n):
    answer = 0
    
    while 1:
        if n <= 7*answer:
            break;
        else:
            answer += 1
    
    return answer