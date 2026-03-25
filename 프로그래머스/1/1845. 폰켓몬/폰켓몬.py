# 260325

def solution(nums):
    answer = 0
    
    # 각 포켓몬 별 개수 저장
    count = set(nums)
    
    # n: 뽑을 수 있는 개수
    n = len(nums) / 2
    
    # 계산
    if len(count) >= n:
        answer = n
    else:
        answer = len(count)
    
    return answer