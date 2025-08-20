def solution(emergency):
    answer = []
    
    for i in emergency:
        rank=1
        for j in emergency:
            if i < j:
                rank += 1
        answer.append(rank)
    
    return answer