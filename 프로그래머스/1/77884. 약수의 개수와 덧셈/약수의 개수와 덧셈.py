# 260421

def solution(left, right):
    answer = 0
    
    def cnt_measure(n):
        cnt = 0
        for i in range(1, n+1):
            if n%i==0:
                cnt+=1
        return cnt
    
    for num in range(left, right+1):
        cnt = cnt_measure(num)
        if cnt%2==0:
            answer += num
        else:
            answer -= num
    
    return answer