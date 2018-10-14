import random
temp = 0
def monopolyworp(temp):
    rand = random.randrange(1, 7)
    rand2 = random.randrange(rand, 7)
    if rand == rand2:
        dubbel = "(Dubbel)"
    else:
        dubbel = ""
        temp = 0
    if dubbel == "(Dubbel)":
        temp = temp + 1
    if temp == 3:
        dubbel = ('Direct naar de gevangenis')
    print(rand, "+", rand2, "=", (rand + rand2), dubbel)
    return temp

gooi = input("Wil je gooien? (ja/nee)")
while gooi == "ja":
    gooi == ""
    temp = monopolyworp(temp)
    gooi = input("Wil je nog een keer gooien? (ja/nee)")

