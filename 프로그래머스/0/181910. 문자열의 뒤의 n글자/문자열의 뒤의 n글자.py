# 260308

def solution(my_string, n):
    answer = ''
    
    index = len(my_string)-n
    answer += my_string[index:]
    
    return answer