# 260517

T = int(input())

for t in range(1, T+1):

    string = input()
    rev_string = string[::-1]
    answer = 0
    if string == rev_string:
        answer = 1

    print("#{} {}".format(t, answer))