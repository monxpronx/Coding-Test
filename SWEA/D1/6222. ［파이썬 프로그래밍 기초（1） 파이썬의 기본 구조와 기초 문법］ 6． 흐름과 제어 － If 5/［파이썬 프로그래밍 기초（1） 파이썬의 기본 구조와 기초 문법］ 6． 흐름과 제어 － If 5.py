# 260616

ch1 = input()
ord1 = ord(ch1)

if ord('a') <= ord(ch1) <= ord('z'):
    ch2 = ch1.upper()
    ord2 = ord(ch2)
elif ord('A') <= ord(ch1) <= ord('Z'):
    ch2 = ch1.lower()
    ord2 = ord(ch2)

print("{}(ASCII: {}) => {}(ASCII: {})".format(ch1, ord1, ch2, ord2))