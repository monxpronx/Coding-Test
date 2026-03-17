# 260317

def solution(arr, flag):
    answer = []
    
    for i in range(len(flag)):
        num = arr[i]
        if flag[i]==True:
            for j in range(num*2):
                answer.append(num)
        else:
            for j in range(num):
                answer.pop()
    
    return answer