# 260214

def solution(numbers):
    answer = 0
    
    mul_max = numbers[0]*numbers[1]
    for num1 in numbers:
        for num2 in numbers:
            if num2 == num1:
                continue
            else:
                if num1*num2 > mul_max:
                    mul_max = num1*num2
    
    answer = mul_max
    
    return answer