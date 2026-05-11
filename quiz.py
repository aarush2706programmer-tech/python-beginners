import random

questions = {
    "2 + 2": "4",
    "5 x 6": "30",
    "10 - 3": "7",
    "9 / 3": "3",
    "7 + 8": "15"
}

selected = random.sample(list(questions.items()), 3)

score = 0

for q, ans in selected:
    try:
        user = input(q + ": ")
        if user == ans:
            score += 1
            print("Good job")
    except:
        print("Error")

print("Score:", score, "/3")


