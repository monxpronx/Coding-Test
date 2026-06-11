# 260611

answer = ""

for num in range(100, 301):

    num = str(num)
    ch1, ch2, ch3 = num[0], num[1], num[2]
    n1, n2, n3 = int(ch1), int(ch2), int(ch3)

    if n1%2==0 and n2%2==0 and n3%2==0:
        answer += str(num)
        answer += ","

answer = answer[:len(answer)-1]
print(answer)