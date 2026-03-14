# 260314

def solution(myString):
    answer = ''
    
    for i in range(len(myString)):
        if myString[i] == 'a':
            answer += 'A'
        elif ord('B') <= ord(myString[i]) <= ord('Z'):
            answer += myString[i].lower()
        else:
            answer += myString[i]
    
    return answer