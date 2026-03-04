# 260304

def solution(a, b):
    answer = 0
    
    num1 = int(str(a)+str(b))
    num2 = 2 * a * b
    answer = max(num1, num2)
    
    return answer