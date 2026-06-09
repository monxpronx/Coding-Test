# 260609

h1 = input()
h2 = input()

winner = ""
if h1 == "가위":
    if h2 == "보":
        winner = "Man1"
    elif h2 == "바위":
        winner = "Man2"
elif h1 == "바위":
    if h2 == "가위":
        winner = "Man1"
    elif h2 == "보":
        winner = "Man2"
else:
    if h2 == "가위":
        winner = "Man2"
    elif h2 == "바위":
        winner = "Man1"

if len(winner) == 0:
    print("Result : Draw")
else:
    print("Result :", winner, "Win!")