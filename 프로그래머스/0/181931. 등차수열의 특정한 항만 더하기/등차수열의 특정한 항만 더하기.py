# 260305

def solution(a, d, included):
    answer = 0
    
    num = a-d # 초기값
    for i in range(len(included)):
        num += d
        if included[i]==True:
            answer += num
            
    return answer