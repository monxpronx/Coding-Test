# 260206

def solution(num, k):
    answer = 0
    flag = 0
    
    num = str(num)
    for i in range(len(num)):
        if num[i] == str(k):
            answer = i+1
            flag = 1
            break
    
    if flag == 0:
        answer = -1
    
    return answer