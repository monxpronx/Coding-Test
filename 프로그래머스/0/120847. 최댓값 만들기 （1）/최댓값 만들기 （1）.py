# 250909

def solution(numbers):
    answer = 0
    
    numbers.sort(reverse=True)  # 내림차순 정렬
    answer = numbers[0] * numbers[1]
    
    return answer