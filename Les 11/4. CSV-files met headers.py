import csv
from itertools import islice
temp = []
artnmr = []
artcd = []
naam = []
vorad = []
prijs = []
index = []
totaal = 0
artikel = []
with open("Data.csv", "r") as data:
    datar = csv.reader(data)
    try:
        for artik in (islice(datar, 1, None)):
            artikel.extend(artik)

            for i in artikel:

                temp.extend(str(i).split(";"))

            artnmr.append(int(temp[0]))
            artcd.append(temp[1])
            naam.append(temp[2])
            vorad.append(int(temp[3]))
            prijs.append(float(temp[4]))
            temp.clear()
            artikel.clear()

    except:

        index = prijs.index(max(prijs))
        print("Het duurste artikel is:", naam[index], "met een prijs van", prijs[index])
        index = vorad.index(min(vorad))
        print("Er zijn slechts", vorad[index], "exemplaren van het artikel met nummer:", artnmr[index])
        for i in vorad:
            totaal = totaal + float(i)
        print("We hebben in totaal", totaal, "producten in ons magazijn liggen.")


