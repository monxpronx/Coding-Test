# 260316

def solution(myString, pat):
    answer = 0
    
    rev = ""
    for ch in myString:
        if ch=='A':
            rev+='B'
            
        else:
            rev+='A'

    if pat in rev:
        answer = 1
            
    return answer