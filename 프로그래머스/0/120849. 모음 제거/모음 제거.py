# 260127

def solution(my_string):
    answer = ''
    
    for str in my_string:
        if str in 'aeiou':
            continue
        answer += str
    
    return answer