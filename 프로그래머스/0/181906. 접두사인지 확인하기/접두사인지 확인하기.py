# 260310

def solution(my_string, is_prefix):
    answer = 0
    
    tmp = []
    for i in range(len(my_string)):
        tmp.append(my_string[:i+1])
    
    if is_prefix in tmp:
        answer = 1
    
    return answer