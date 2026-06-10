# 260610

T = int(input())

for t in range(1, T+1):

    ch = input()
    if ch in "abcdefghijklmnopqrstuvwxyz":
        print("#{} {} 는 소문자 입니다.".format(t, ch))
    else:
        print("#{} {} 는 대문자 입니다.".format(t, ch))