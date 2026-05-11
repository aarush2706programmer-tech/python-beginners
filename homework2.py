a=["Advik","Divyandu","Prathmesh","Vihaan","Nitant"]
for i in a:
    print(i)

best = a[3]
print(f"My bestest friend is {best}")

text = "Keeping   our surroundings   clean is   important   for health   and happiness.  Every day,   I try   to keep   my room   neat   and organized.  I put my books   on the shelf,   throw waste   in the dustbin,   and wipe   my desk.  Cleaning also   teaches responsibility   and discipline.  When places are clean,   they look beautiful   and feel comfortable.  It also prevents   diseases   and keeps the air   fresh.  We should not litter   in public places   and must follow   good habits.  If everyone cleans   a little,   the whole world   becomes a better place.  Cleanliness is   a simple step   toward a bright   and healthy life   for all people."
cleaned = " ".join(text.split())
print(cleaned)
print(cleaned.count("and"))
print(cleaned.split(","))
