# 260306

def solution(l, r):
    answer = []
    
    for num in range(l, r+1):
        num = str(num)
        flag = 0
        for ch in num:
            if ch not in ['5', '0']:
                flag = 1
                break
        if flag == 0:
            answer.append(int(num))
            
    answer.sort()
    if len(answer)==0:
        answer.append(-1)
    
    return answer