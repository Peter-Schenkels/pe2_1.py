leeftijd = int(input("Wat is je leeftiid:"))
if leeftijd >= 18:
    paspoort = input("Heb je een paspoort (ja/nee):")
    if paspoort == "ja":
        print("Je mag stemmen!")
    else:
        if paspoort == "nee":
            print("Je mag niet stemmen.")

        else:
            print("Je antwoord is fout!")
else:
    print("Je bent te jong om te stemmen")


#Als je maar 1x if mag gebruiken

leeftijd = int(input("Wat is je leeftiid:"))
paspoort = input("Heb je een paspoort (ja/nee):")
if leeftijd >=18 and paspoort == "ja":
    print("Je mag stemmen!")
else:
    print("Je mag niet stemmen of je hebt de verkeerde gegevens ingevuld!")

