import datetime
import csv
naam = ""
vandaag = datetime.datetime.today()
s = vandaag.strftime("%a %d %b %Y")

bestand = 'inloggers.csv'
with open(bestand, "r+") as lijst:
    while naam != "einde":
        lijst.read()
        naam = input("Wat is je achternaam? ")
        if naam == "einde":
            exit()
        voorl = input("Wat zijn je voorletters? ")
        gbdatum = input("Wat is je geboortedatum? ")
        email = input("Wat is je e-mail adres? ")
        lijst.write(s +";"+voorl +";"+ naam +";"+ gbdatum +";"+ email+ "\n")

#wanneer de volgende persoon inlogt is onbekend, dus schrijf meteen naar file