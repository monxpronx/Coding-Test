# 260404

price = int(input())
cnt = int(input())

total = 0
for i in range(cnt):
    p, c = map(int, input().split())
    total += (p*c)

if price == total:
    print("Yes")
else:
    print("No")