# 260526

the_list = [1,2,3,4,3,2,1]

def set_list(the_list):
    the_list = set(the_list)
    return list(the_list)

print(the_list)
print(set_list(the_list))