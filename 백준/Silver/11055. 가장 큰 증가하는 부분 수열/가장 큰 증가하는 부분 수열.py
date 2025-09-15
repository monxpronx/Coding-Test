import sys

input = sys.stdin.readline

n = int(input().strip())  # 수열의 크기 N
arr = list(map(int, input().split()))  # 수열 A (길이 N)

dp = [0] * n

for i in range(n):
    dp[i] = arr[i]

    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + arr[i])

print(max(dp))
