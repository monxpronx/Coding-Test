# 260329

def solution(clothes):
    answer = 1
    
    dic = {}
    for c in clothes:
        if c[1] in dic:
            dic[c[1]] += 1
        else:
            dic[c[1]] = 1
            
    for d in dic:
        answer *= (dic[d]+1)
    answer -= 1
    
    return answer