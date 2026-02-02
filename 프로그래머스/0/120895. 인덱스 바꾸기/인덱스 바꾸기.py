# 260202

def solution(my_string, num1, num2):
    answer = ''
    
    # num1, num2 순서 고정
    if num1 > num2:
        tmp = num1
        num1 = num2
        num2 = tmp
    
    for i in range(len(my_string)):
        if i == num1:
            answer += my_string[num2]
        elif i == num2:
            answer += my_string[num1]
        else:
            answer += my_string[i]
    
    return answer