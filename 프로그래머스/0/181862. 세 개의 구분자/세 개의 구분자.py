# 260317

def solution(myStr):
    answer = []
    
    for ch in "abc":
        if ch in myStr:
            myStr = myStr.replace(ch, " ")
    
    answer = myStr.split()
    if len(answer)==0:
        answer.append('EMPTY')
    
    return answer