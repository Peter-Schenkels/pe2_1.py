Zin = input("Voer een zin in:")


def gemiddelde(zin):
    lijst = []
    lijst.extend(zin.split(" "))
    totaal = 0
    print(lijst)
    for i in lijst:
        totaal += len(i)
    print(totaal / len(lijst))


gemiddelde(Zin)