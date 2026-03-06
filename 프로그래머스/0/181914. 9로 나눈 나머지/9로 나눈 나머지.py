# 260306

def solution(number):
    answer = 0
    
    n = str(number)
    num = 0
    for i in n:
        num += int(i)
    
    answer = num%9
    
    return answer