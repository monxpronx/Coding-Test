# 260319

def solution(arr, delete_list):
    answer = []
    
    for n in delete_list:
        if n in arr:
            arr.remove(n)
            
    answer = arr
    
    return answer