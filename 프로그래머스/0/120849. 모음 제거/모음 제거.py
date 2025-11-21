# 251121

def solution(my_string):
    answer = ''
    
    for ch in my_string:
        if ch in ('a','e','i','o','u'):
            continue
        answer += ch
    
    return answer