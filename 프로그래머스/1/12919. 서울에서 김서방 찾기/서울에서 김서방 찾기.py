# 260420

def solution(seoul):
    answer = ''
    
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            break
    
    answer += "김서방은 {}에 있다".format(i)
    
    return answer