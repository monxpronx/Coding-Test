# 260221

def solution(score):
    answer = [1] * len(score)
    
    mean_list = []
    for i in range(len(score)):
        mean = (score[i][0] + score[i][1]) / 2
        mean_list.append(mean)
        
    for i in range(len(score)): # 비교기준원소 i
        for j in range(len(score)): # 비교대상원소 j
            if mean_list[i] < mean_list[j]:
                answer[i]+=1
    
    return answer