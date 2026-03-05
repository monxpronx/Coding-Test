# 260305

def solution(num_list):
    answer = 0
    str_even = ""
    str_odd = ""
    
    for num in num_list:
        if num%2==0:
            str_even += str(num)
        else:
            str_odd += str(num)
            
    answer = int(str_even) + int(str_odd)
    
    return answer