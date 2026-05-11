# 260511

a, b = map(int, input().split())

if a==1 and b==2:
    answer = 'B'
elif a==1 and b==3:
    answer = 'A'
elif a==2 and b==1:
    answer = 'A'
elif a==3 and b==1:
    answer = 'B'
elif a==2 and b==3:
    answer = 'B'
else:
    answer = 'A'

print(answer)