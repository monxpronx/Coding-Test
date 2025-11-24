# 251124
import math

def solution(n):
    answer = 0
    num=1
    
    while 1:
        
        if math.factorial(num) > n:
            answer = num-1
            break
    
        num+=1
    
    return answer