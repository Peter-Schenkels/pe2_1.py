

def standaardtarief(afstandKM):
    if afstandKM <= 50:
       totaal = afstandKM * 0.80
    else:

        totaal = afstandKM * 0.60 + 15
    if afstandKM <= 0:
        totaal = 0
    return totaal

Afstandkm = (int(input("Voeg hier je aftand in kilometers in: ")))
Leeftijd = (int(input("Voeg hier je leeftijd in: ")))
weekend = (input("Is deze rit in het weekend? (y/n): "))

if weekend == "y":
    weekend = True
elif weekend == "n":
    weekend = False
else:
    print("error")


def ritprijs(leeftijd, weekendrit):
    ritprijs = 1.0
    if leeftijd <= 65 or leeftijd < 12:
        ritprijs = ritprijs * 0.70


    if leeftijd >= 65 or leeftijd < 12 and weekendrit == True:
        ritprijs = ritprijs  * 0.65

    if leeftijd <= 65 or leeftijd > 12 and weekendrit == True:
        ritprijs = ritprijs * 0.60
    return ritprijs



print("Je rit prijs is: €", "%.2f" %(ritprijs(Leeftijd, weekend)* standaardtarief(Afstandkm)))



