# 260312

def solution(str_list):
    answer = []
    
    index_first_l = 0
    index_first_r = 0
    flag_l = 0
    flag_r = 0
    for i in range(len(str_list)):
        if str_list[i] == 'l' and flag_l == 0:
            index_first_l = i
            flag_l = 1
        if str_list[i] == 'r' and flag_r == 0:
            index_first_r = i
            flag_r = 1
        if flag_l == 1 and flag_r == 1:
            break
    if flag_l == 1 and flag_r == 1:
        if index_first_l < index_first_r:
            answer = str_list[:index_first_l]
        elif index_first_r < index_first_l:
            answer = str_list[index_first_r+1:]
    elif flag_l == 1:
        answer = str_list[:index_first_l]
    elif flag_r == 1:
        answer = str_list[index_first_r+1:]
    
    return answer