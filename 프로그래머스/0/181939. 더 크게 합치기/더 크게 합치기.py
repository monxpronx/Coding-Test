# 260304

def solution(a, b):
    answer = 0
    
    a = str(a)
    b = str(b)
    
    num1 = int(a+b)
    num2 = int(b+a)
    answer = max(num1, num2)
    
    return answer