# 260423

def solution(s):
    answer = True
    
    if len(s) not in [4,6]:
        answer = False
    else:
        for ch in s:
            if ch.isdigit():
                pass
            else:
                answer = False
                break
    
    return answer