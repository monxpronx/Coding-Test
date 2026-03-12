# 260312

def solution(arr, intervals):
    answer = []
    
    tmp1 = []
    tmp2 = []
    
    tmp1 = arr[intervals[0][0]:intervals[0][1]+1]
    tmp2 = arr[intervals[1][0]:intervals[1][1]+1]
    answer = tmp1 + tmp2
    
    return answer