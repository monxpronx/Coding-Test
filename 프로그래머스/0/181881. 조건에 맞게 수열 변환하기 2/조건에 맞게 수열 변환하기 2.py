# 260313

def solution(arr):
    answer = 0
    
    def make_next(arr):
        next_arr = []
        for i in range(len(arr)):
            next_arr.append(arr[i])
            if (50<=arr[i]) and (arr[i]%2==0):
                next_arr[i]/=2
            elif (arr[i]<50) and (arr[i]%2==1):
                next_arr[i] = arr[i]*2+1
        return next_arr
    
    while 1:
        flag = 0
        next_arr = make_next(arr)
        for i in range(len(arr)):
            if arr[i] != next_arr[i]:
                flag = 1
                break
        if flag == 0:
            break
        answer+=1
        arr = next_arr[:]
    
    return answer