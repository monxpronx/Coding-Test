# 251122

def solution(age):
    answer = ''
    
    while age > 0:
        answer = chr((age%10)+ord('a')) + answer
        age = age//10
    
    return answer