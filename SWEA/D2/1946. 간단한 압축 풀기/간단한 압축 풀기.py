# 260515

T = int(input())

for i in range(1, T+1):

    n = int(input())
    string = ""

    for _ in range(n):
        ch, ch2 = input().split()
        cnt = int(ch2)
        string += (ch * cnt)

    print("#{}".format(i))
    for j in range(len(string)//10):
        print(string[10*j:10*(j+1)])
    print(string[10*(j+1):])