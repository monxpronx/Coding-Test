# 251119

def solution(my_string):
    answer = ''
    

    # 반복문을 이용해서, 각 반복마다 앞에다 더해주는 방식
    for str in my_string:
        answer = str + answer
    
    return answer