# 250910

def solution(s1, s2):
    answer = 0
    
    for s1_el in s1:
        if s1_el in s2:
            answer+=1
    
    return answer