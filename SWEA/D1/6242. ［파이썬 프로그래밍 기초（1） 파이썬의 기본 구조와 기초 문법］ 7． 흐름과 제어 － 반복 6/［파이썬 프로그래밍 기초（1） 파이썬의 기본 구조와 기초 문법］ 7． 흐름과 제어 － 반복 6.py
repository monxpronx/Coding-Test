# 260623

temp = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']

dict = {
    'A': 0,
    'O': 0,
    'B': 0,
    'AB': 0
}

for t in temp:
    if t == 'A':
        dict['A'] += 1
    elif t == 'O':
        dict['O'] += 1
    elif t == 'B':
        dict['B'] += 1
    else:
        dict['AB'] += 1

print(dict)