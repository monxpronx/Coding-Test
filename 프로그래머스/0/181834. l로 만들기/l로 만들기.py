# 260321

def solution(myString):
    answer = ''
    
    for ch in myString:
        if ord(ch) < ord('l'):
            answer += 'l'
        else:
            answer += ch
    
    return answer