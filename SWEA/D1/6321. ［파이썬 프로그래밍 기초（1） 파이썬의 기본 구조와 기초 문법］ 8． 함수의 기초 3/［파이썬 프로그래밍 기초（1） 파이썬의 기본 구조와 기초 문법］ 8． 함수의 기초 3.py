# 260601

def is_prime(n):
    for i in range(2, n):
        cnt = 0
        if n%i==0:
            cnt+=1
    if cnt == 0:
        print("소수입니다.")
    else:
        print("소수가 아닙니다.")

n = int(input())
is_prime(n)