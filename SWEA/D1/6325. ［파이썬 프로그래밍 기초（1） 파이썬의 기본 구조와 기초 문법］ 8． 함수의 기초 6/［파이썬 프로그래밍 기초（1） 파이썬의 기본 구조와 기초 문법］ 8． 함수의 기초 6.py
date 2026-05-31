# 260531

my_string = [2,4,6,8,10]

def find_n(n, my_string):
    tmp = ""
    if n in my_string:
        tmp += "True"
    else:
        tmp += "False"
    return tmp

print(my_string)
print("5 =>", find_n(5, my_string))
print("10 =>", find_n(10, my_string))