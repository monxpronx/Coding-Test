# 251119

def solution(numbers):
    answer = 0
    
    numbers.sort()
    answer = numbers[-1] * numbers[-2]
    
    return answer

'''
정렬해서 쉽게 풀자..
'''