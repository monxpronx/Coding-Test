# 260301

def solution(common):
    answer = 0
    
    flag = 0 ### 우선 등차수열이라 가정
    diff = common[1] - common[0]
    for i in range(len(common)-1):
        if common[i+1] - common[i] != diff:
            flag = 1
            break
            
    ### flag=0(등차) / flag=1(등비) ###
    if flag == 0:
        answer = common[len(common)-1] + diff
    else:
        answer = common[len(common)-1] * (common[1]//common[0])
    
    return answer