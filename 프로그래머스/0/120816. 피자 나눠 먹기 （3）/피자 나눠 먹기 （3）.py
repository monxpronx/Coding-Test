# 250910

def solution(slice, n):
    answer = 0
    
    while 1:
        if n <= slice*answer:
            break;
        else:
            answer += 1
    
    return answer