# 251124

def solution(num_list, n):
    answer = [[]]
    
    # 몇 개의 덩어리인지
    loaf = len(num_list) // n
    
    idx=0
    for i in range(loaf):
        if i>0:
            answer.append([])
            # 새로운 행을 만들어줘야함!
        
        for j in range(n):
            answer[i].append(num_list[idx])
            idx+=1
            
    return answer