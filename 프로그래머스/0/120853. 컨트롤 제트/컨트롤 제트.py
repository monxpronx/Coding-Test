# 251125

def solution(s):
    answer = 0
    before_ch = 0
    
    s_list = s.split(' ')
    
    for ch in s_list:
        if ch == 'Z':
            answer -= int(before_ch)
            before_ch = 0
        else:
            answer += int(ch)
            before_ch = ch
    
    return answer