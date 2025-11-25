# 251125

def solution(bin1, bin2):
    answer = ''
    
    num1 = int(bin1, 2)
    num2 = int(bin2, 2)
    num = num1 + num2
    
    num = bin(num)
    answer = num[2:]
    
    return answer