# 260308

def solution(intStrs, k, s, l):
    answer = []
    
    for strs in intStrs:
        str_num = strs[s:s+l]
        num = int(str_num)
        if num > k:
            answer.append(num)
    
    return answer