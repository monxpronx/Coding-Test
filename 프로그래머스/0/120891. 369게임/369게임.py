# 251122

def solution(order):
    answer = 0
    
    while order>0:
        num = order%10
        if num in [3,6,9]:
            answer += 1
        order = order // 10
    
    return answer