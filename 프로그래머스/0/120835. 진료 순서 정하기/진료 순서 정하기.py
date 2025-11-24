# 251124

def solution(emergency):
    answer = []
    
    answer = [1] * len(emergency)
    
    for i in range(len(emergency)): # 비교기준원소(인덱스))
        cnt=0
        for j in range(len(emergency)): # 비교대상원소(인덱스)
            if emergency[i] < emergency[j]:
                answer[i] += 1
    
    return answer