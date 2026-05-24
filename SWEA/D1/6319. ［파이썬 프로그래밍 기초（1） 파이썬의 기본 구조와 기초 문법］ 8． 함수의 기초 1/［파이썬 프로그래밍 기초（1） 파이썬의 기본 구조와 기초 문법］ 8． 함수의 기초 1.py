# 260524

string = input()

def print_rev(string):
    string_rev = string[::-1]
    return string_rev

print(print_rev(string))
if string == print_rev(string):
    print("입력하신 단어는 회문(Palindrome)입니다.")