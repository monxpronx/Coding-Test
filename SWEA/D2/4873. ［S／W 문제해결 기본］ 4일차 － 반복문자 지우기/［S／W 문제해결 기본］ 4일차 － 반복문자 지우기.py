# 260520

T = int(input())

for t in range(1, T+1):

    string = input()

    while 1:
        
        string_re = ""
        flag = 0
        for i in range(len(string)-1):
            if string[i] == string[i+1]:
                string_re += string[:i]
                string_re += string[i+2:]
                flag = 1
                break
        
        if flag == 0:
            break

        string = string_re

    print("#{} {}".format(t, len(string)))