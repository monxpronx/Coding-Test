def solution(N, number):
    
    dp = [set() for _ in range(9)]
    
    for i in range(1, 9):
        
        # 그냥 이어붙인 수 추가
        dp[i].add(int(str(N) * i))
        
        # 사칙연산한 수 추가
        for j in range(1, i):
            for n1 in dp[j]:
                for n2 in dp[i - j]:
                    dp[i].add(n1+n2)
                    dp[i].add(n1-n2)
                    dp[i].add(n1*n2)
                    if n2 != 0:
                        dp[i].add(n1//n2)
        
        if number in dp[i]:
            return i
    
    return -1