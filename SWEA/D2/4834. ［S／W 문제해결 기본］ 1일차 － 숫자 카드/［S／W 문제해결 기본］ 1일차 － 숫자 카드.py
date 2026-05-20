# 260520

T = int(input())

for t in range(1, T+1):

    dict = {
        '0': 0, '1': 0, '2': 0, '3': 0, '4': 0,
        '5': 0, '6': 0, '7': 0, '8': 0, '9': 0
    }

    N = int(input())
    num_str = input()

    max_num = -1
    max_num_cnt = 0

    for ch in num_str:
        
        for key in dict:
            if ch == key:
                dict[key] += 1
                if dict[key] > max_num_cnt:
                    max_num = int(key)
                    max_num_cnt = dict[key]
                elif (dict[key] == max_num_cnt) and (int(key) > max_num):
                    max_num = int(key)
                    max_num_cnt = dict[key]

    print("#{} {} {}".format(t, max_num, max_num_cnt))