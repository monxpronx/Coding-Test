# 260318

def solution(arr):
    answer = []
    num=0
    
    ex = [2,4,8,16,32,64,128,256,512,1024]
    length = len(arr)
    
    for i in range(len(ex)):
        if ex[i] < length < ex[i+1]:
            num = ex[i+1]
            break
            
    for n in arr:
        answer.append(n)
        
    while len(answer) < num:
        answer.append(0)
    
    return answer