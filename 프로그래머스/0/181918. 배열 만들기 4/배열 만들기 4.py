# 260306

def solution(arr):
    stk = []
    
    i=0
    while i < len(arr):
        if len(stk)==0:
            stk.append(arr[i])
            i+=1
        elif len(stk)!=0 and stk[len(stk)-1] < arr[i]:
            stk.append(arr[i])
            i+=1
        else:
            stk = stk[:len(stk)-1]
    
    return stk