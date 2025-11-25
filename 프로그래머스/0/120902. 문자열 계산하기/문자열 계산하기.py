# 251125

def solution(my_string):
    answer = 0
    before_ch = ''
    
    str_list = my_string.split(' ')
    answer = int(str_list[0])
    
    for ch in str_list:
        if ch == '+':
            before_ch = '+'
        elif ch == '-':
            before_ch = '-'
        else:
            if before_ch == '+':
                answer += int(ch)
            else:
                if before_ch == '-':
                    answer -= int(ch)
            
    
    return answer