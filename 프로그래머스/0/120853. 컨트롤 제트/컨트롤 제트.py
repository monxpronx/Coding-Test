# 260129

def solution(s):
    answer = 0
    tmp = 0
    
    s = s.split()
    
    for str in s:
        if str == 'Z':
            answer -= int(tmp)
        else:
            answer += int(str)
        tmp = str
    
    return answer