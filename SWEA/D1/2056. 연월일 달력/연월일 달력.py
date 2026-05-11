# 260511

T = int(input())

for i in range(T):

    string = input()
    year = int(string[:4])
    month = int(string[4:6])
    date = int(string[6:])

    flag = 0
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if date==0 or date > 31:
            flag = 1
    elif month in [4, 6, 9, 11]:
        if date==0 or date > 30:
            flag = 1
    elif month == 2:
        if date==0 or date > 28:
            flag = 1
    else:
        flag = 1
    
    if flag == 0:
        print("#{} {:04d}/{:02d}/{:02d}".format(i+1, year, month, date))
    else:
        print("#{} -1".format(i+1))