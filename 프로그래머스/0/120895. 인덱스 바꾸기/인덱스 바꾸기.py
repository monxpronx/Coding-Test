# 251122

def solution(my_string, num1, num2):
    answer = ''
    
    for i in range(len(my_string)):
        if i==num1:
            answer += my_string[num2]
            continue
        elif i==num2:
            answer += my_string[num1]
            continue
        answer += my_string[i]
    
    return answer