# 260403

hour, min = map(int, input().split())

if min < 45:
    hour -= 1
    min = (min+60) - 45
else:
    min -= 45

# 예외조건
if hour < 0:
    hour = 23

print(hour, min)