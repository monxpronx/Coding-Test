# 260403

a, b, c = map(int, input().split())

if a==b==c:
    total = 10000 + a*1000
elif a==b:
    total = 1000 + a*100
elif b==c:
    total = 1000 + b*100
elif c==a:
    total = 1000 + c*100
else:
    total = max(a,b,c)*100

print(total)