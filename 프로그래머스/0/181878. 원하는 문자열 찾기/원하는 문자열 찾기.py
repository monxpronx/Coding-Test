# 260313

def solution(myString, pat):
    answer = 0
    
    low_pat = pat.lower()
    low_string = myString.lower()
    
    if low_pat in low_string:
        answer = 1    
    
    return answer