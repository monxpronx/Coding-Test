# 260608

tmp = ""
for n in range(1, 200+1):
    if (n % 7 == 0) and (n % 5 !=0):
        tmp += str(n)
        tmp += ","

tmp = tmp[:len(tmp)-1]
print(tmp)