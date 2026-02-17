# 260217

def solution(spell, dic):
    answer = 2
    
    for d in dic:
        tmp_list = [0]*len(spell)
        for i in range(len(spell)):
            if spell[i] in d:
                tmp_list[i] = 1
        if sum(tmp_list) == len(spell):
            answer=1
            break
    
    return answer