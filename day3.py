names = ["aarush","  vihaan  ","ADVIK","divyandu"]
for i in names:
    """print(i.strip())
    print(i.title())"""
    print(i.strip().title())
    print(i.lower().count("a"))

"""for i in names:
    print(i.count("a"))"""

#dictionary
my_dict = {"name":"Advik","age":15,"city":"Pune"}
print(my_dict["name"])

player={"names":"Vihaan","level":1,"health":10,"weapon":"bow"}
print(player["names"])
print(player["health"])
player["health"]=100
print(player["health"])
#player["armor"]=80
print(player.get("armor"))

for i, j in player.items():
    print(i,j)

player2={{"names":"Nitant","level":2,"health":20,"weapon":"sword"},{"names":"Prathmesh","level":3,"health":30,"weapon":"axe"}}
for i in player2:
    print(i)

player3={"names":{"player1":"Advik","player2":"Vihaan","player3":"Nitant","player4":"Prathmesh"},"level":{"player1":1,"player2":2,"player3":3,"player4":4},"health":{"player1":10,"player2":20,"player3":30,"player4":40},"weapon":{"player1":"bow","player2":"sword","player3":"axe","player4":"spear"}}
for i, j in player3.items():
    print(i,j)

print(player3["names"]["player1"])
print(player3["health"]["player1"])