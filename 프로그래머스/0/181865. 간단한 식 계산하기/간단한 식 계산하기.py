# 260316

def solution(binomial):
    answer = 0
    
    tmp = binomial.split()
    num1 = int(tmp[0])
    num2 = int(tmp[2])
    op = tmp[1]
    
    if op == "+":
        answer = num1+num2
    elif op == "-":
        answer = num1-num2
    else:
        answer = num1*num2
    
    return answer