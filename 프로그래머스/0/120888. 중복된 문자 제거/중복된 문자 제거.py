# 251122

def solution(my_string):
    answer = ''
    
    for ch in my_string:
        if ch in answer:
            continue
        else:
            answer += ch
    
    return answer