# 260311

def solution(num_list):
    answer = 0
    flag = 0
    
    for i in range(len(num_list)):
        if num_list[i] < 0:
            answer = i
            flag = 1
            break
    
    if flag == 0:
        answer = -1
    
    return answer