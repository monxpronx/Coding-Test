# 260403

hour, min = map(int, input().split())
t = int(input())

hour += (t//60)
min += (t%60)

if min >= 60:
    hour += 1
    min -= 60
    
if hour >= 24:
    hour -= 24

print(hour, min)