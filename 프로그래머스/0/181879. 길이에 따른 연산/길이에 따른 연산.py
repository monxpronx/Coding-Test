# 260313

def solution(num_list):
    answer = 0
    
    if 11 <= len(num_list):
        answer = sum(num_list)
    else:
        answer=1
        for num in num_list:
            answer *= num
    
    return answer