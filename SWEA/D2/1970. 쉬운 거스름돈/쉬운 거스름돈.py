# 260519

T = int(input())

for t in range(1, T+1):

    dict = {
        '50000': 0,
        '10000': 0,
        '5000': 0,
        '1000': 0,
        '500': 0,
        '100': 0,
        '50': 0,
        '10': 0
    }

    N = int(input())

    for key in dict:
        key_n = int(key)
        dict[key] += (N//key_n)
        N -= (dict[key] * key_n)

    print("#{}".format(t))
    answer = ""
    for key in dict:
        answer += str(dict[key])
        answer += " "
    print(answer)