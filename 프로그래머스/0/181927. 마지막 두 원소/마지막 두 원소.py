# 260305

def solution(num_list):
    answer = []
    
    # 일단 다 추가
    for num in num_list:
        answer.append(num)
    
    last = num_list[len(num_list)-1]
    last2 = num_list[len(num_list)-2]
    
    if last > last2:
        answer.append(last-last2)
    else:
        answer.append(last*2)
    
    return answer