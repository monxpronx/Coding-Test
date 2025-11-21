# 251121

def solution(my_string, letter):
    answer = ''
    
    for ch in my_string:
        if letter!=ch:
            answer+=ch
    
    return answer