# 260205

def solution(my_string):
    answer = 0
    temp_cal = ''
    
    str_to_list = my_string.split() ### 문자열->리스트로 split
    
    for el in str_to_list:
        
        if el == '+':
            temp_cal = '+'
        
        elif el == '-':
            temp_cal = '-'
        
        else:
            if temp_cal == '+':
                answer += int(el)
            elif temp_cal == '-':
                answer -= int(el)
            else:
                answer = int(el)
    
    return answer