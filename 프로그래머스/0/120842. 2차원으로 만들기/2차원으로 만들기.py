# 260121

def solution(num_list, n):
    answer = [[]]
    
    i=0
    for num in num_list:
        if len(answer[i]) == n:
            i += 1
            answer.append([])
        answer[i].append(num)
    
    return answer