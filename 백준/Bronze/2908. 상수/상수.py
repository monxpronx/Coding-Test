# 260409

s1, s2 = input().split()

n1 = int(s1[::-1])
n2 = int(s2[::-1])
print(max(n1, n2))