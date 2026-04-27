# 260427

def solution(s):
    answer = ''
    
    idx = 0
    for ch in s:
        if ch != ' ' and idx%2 == 0:
            answer += ch.upper()
        elif ch != ' ' and idx%2 == 1:
            answer += ch.lower()
        else:
            answer += ch
            idx = -1
        idx += 1
    
    return answer