# 260421

def solution(s):
    answer = ''
    
    s_list = list(s)
    length = len(s_list)
    for i in range(length-1):
        for j in range(length-1-i):
            if s_list[j] < s_list[j+1]:
                tmp = s_list[j]
                s_list[j] = s_list[j+1]
                s_list[j+1] = tmp
    
    answer = ''.join(s_list)
    
    return answer