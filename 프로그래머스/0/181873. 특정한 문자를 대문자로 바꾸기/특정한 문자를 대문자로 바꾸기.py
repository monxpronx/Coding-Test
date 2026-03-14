# 260314

def solution(my_string, alp):
    answer = ''
    
    for ch in my_string:
        if ch==alp:
            answer += alp.upper()
        else:
            answer += ch
    
    return answer