#DICTIONARY HOMEWORK
game = {
    "title":   "Dragon Quest",
    "level":   7,
    "health":  85,
    "items":   ["shield", "potion", "map"],
    "alive":   True,
}
print(game["title"])
new_health= game["health"]=60
print(game["health"])
game["coins"] = 150
print(game["coins"])

for i, j in game.items():
    print(i,j)

person = {"name": "Rahul", "age": 15, "city": "Delhi"}
"""print(person[0])
This crashes because dictionaries do not support indexing.
Therefore the correct code is : print(person["name"])"""

profile = {"name": "Aryan", "age": 13}
coins = profile.get("coins", 0)
print("Coins:", coins)
city = profile.get("city", "Unknown")
print("City:", city)

school = {
    "Aryan": {"maths": 88, "science": 92, "english": 79},
    "Priya": {"maths": 95, "science": 87, "english": 91},
}
print(school["Priya"]["science"])

for i,j in school.items():
    print(i,j)

my_game_character = {"name": "Lara", "level": 5, "health": 80, "weapons":["sword"],"coins": 100}
for i,j in my_game_character.items():
    print(i,j)

players = {
    "Rohit": {"runs": 72, "balls": 48, "4s": 8, "6s": 3},
    "Virat": {"runs": 88, "balls": 61, "4s": 9, "6s": 2},
    "Dhoni": {"runs": 45, "balls": 30, "4s": 3, "6s": 2},
    "Rahul": {"runs": 60, "balls": 50, "4s": 5, "6s": 1},
    "Gill": {"runs": 232, "balls": 35, "4s": 6, "6s": 1}
}
print(players)
print(players["Gill"]["runs"])
total_runs = players["Rohit"]["runs"] + players["Virat"]["runs"] + players["Dhoni"]["runs"] + players["Rahul"]["runs"] + players["Gill"]["runs"]
print("Total runs scored by all players:", total_runs)
strike_rate = (players["Rohit"]["runs"] / players["Rohit"]["balls"]) * 100
print("Rohit's strike rate:", strike_rate)
strike_rate = (players["Virat"]["runs"] / players["Virat"]["balls"]) * 100
print("Virat's strike rate:", strike_rate)
strike_rate = (players["Dhoni"]["runs"] / players["Dhoni"]["balls"])
print("Dhoni's strike rate:", strike_rate)
strike_rate = (players["Rahul"]["runs"] / players["Rahul"]["balls"])
print("Rahul's strike rate:", strike_rate)
strike_rate = (players["Gill"]["runs"] / players["Gill"]["balls"])
print("Gill's strike rate:", strike_rate)


#FUNCTION HOMEWORK
#The blank should give the discount of 10%
def calculate_price(price, discount = 10):
    saving = price * (discount / 100)
    return price - saving

print(calculate_price(500))         # should print 450.0
print(calculate_price(500, 20))    # should print 400.0
print(calculate_price(800))         # should print 720.0

def sum_of_squares(a,b):
    print(a**2 + b**2)

sum_of_squares(3,4)   # should print 25

def get_grade(score,passing_score = 40):
    if score >= passing_score:
        return "Pass"
    else:
        return "Fail"

def letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def full_report(names,scores):
     avg = sum(scores) / len(scores)
     grade = letter_grade(avg)
     result = get_grade(avg)

     print("Report for", names)
     print("Average Score:", avg)
     print("Result:", result)
     print("Letter grade:", grade)
full_report("Aryan", [85, 92, 78])  # should print the report for Aryan

