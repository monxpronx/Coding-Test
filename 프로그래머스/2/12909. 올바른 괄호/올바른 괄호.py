# 260509

def solution(s):
    answer = True

    stack = []
    
    for ch in s:
        if ch=='(':
            stack.append(0)
        else:
            if len(stack)==0:
                return False
            stack.pop()
    
    if len(stack)!=0:
        answer = False
    
    return answer