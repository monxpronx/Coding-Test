# 260413

arr = []
len_arr = []
for i in range(5):
    arr.append(list(input()))
    len_arr.append(len(arr[i]))

myString = ""
for j in range(15):
    for i in range(5):
        if j < len_arr[i]:
            myString += arr[i][j]

print(myString)