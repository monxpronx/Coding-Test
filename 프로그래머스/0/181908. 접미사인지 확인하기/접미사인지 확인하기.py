# 260309

def solution(my_string, is_suffix):
    answer = 0
    
    tmp = []
    for i in range(len(my_string)):
        tmp.append(my_string[i:])
    
    if is_suffix in tmp:
        answer = 1
    
    return answer