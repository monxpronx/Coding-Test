# 260221

def solution(numlist, n):
    answer = []
    
    while len(numlist) > 0:
        min_diff = float('inf')
        min_diff_num = 0
        for num in numlist:
            if (max(num,n) - min(num,n)) < min_diff:
                min_diff = max(num,n) - min(num,n)
                min_diff_num = num
            elif (max(num,n) - min(num,n)) == min_diff:
                min_diff_num = max(min_diff_num, num)
        answer.append(min_diff_num)
        numlist.remove(min_diff_num)
    
    return answer