# 251121

def solution(s1, s2):
    answer = 0
    
    for s_1 in s1:
        for s_2 in s2:
            if s_1 == s_2:
                answer += 1
                break
    
    return answer