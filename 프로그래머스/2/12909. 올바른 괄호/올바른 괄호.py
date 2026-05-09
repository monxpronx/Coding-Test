# 260509

def solution(s):
    answer = True
    flag = 0

    for ch in s:
        
        if ch == '(':
            flag += 1
        elif ch == ')':
            flag -= 1
        
        if flag < 0:
            answer = False
            break
            
    if flag != 0:
        answer = False
    
    return answer