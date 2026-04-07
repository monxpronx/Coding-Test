# 260407

students = []
for _ in range(28):
    n = int(input())
    students.append(n)

for i in range(1, 30+1):
    if i not in students:
        print(i)