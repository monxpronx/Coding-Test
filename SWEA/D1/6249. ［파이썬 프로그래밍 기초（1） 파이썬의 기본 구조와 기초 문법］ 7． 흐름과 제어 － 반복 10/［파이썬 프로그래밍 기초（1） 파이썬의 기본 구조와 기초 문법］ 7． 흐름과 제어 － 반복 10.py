# 260524

N = int(input())

tmp = ""
for i in range(10):
    tmp += str(i)
    tmp += " "
print(tmp)

count = [0] * 10
N_str = str(N)
for ch in N_str:
    for i in range(10):
        if ch == str(i):
            count[i] += 1
print(*count)