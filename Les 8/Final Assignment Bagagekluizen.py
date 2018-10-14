file = open("kluissleutels.txt", "r+")
keuze = int(input("1: Ik wil weten hoeveel kluizen nog vrij zijn \n 2: Ik wil een nieuwe kluis  \n 3: Ik wil even iets uit mijn kluis halen  \n 4: Ik geef mijn kluis terug \n"))

gegevens = []
sort = []
wachtwoorden = []
gebruikers = []
kluisIndex = 0
wachtwoordIndex = 0


gegevens = str(file.read())


gegevens = gegevens.splitlines()
gegevens.sort()
open("kluissleutels.txt").close()







for i in gegevens:
    sort.extend(i.split(';'))
    wachtwoorden.extend(i.split(";"))
    gebruikers.extend(i.split(";"))


for i in gebruikers:
    if len(i) > 2 or len(i) == 0:
        gebruikers.remove(i)

for i in wachtwoorden:
    if len(i) != 4:
        wachtwoorden.remove(i)


kluisjes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for i in sort:
    if len(i) <= 2 and i != "":

        i = int(i)
        kluisjes.remove((i))


if keuze == 1:
   print("Aantal kluisjes: ", len(kluisjes))

elif keuze == 2:



    print("Dit zijn alle beschikbare kluisjes:", kluisjes)
    nummer =  eval(input("Welk kluisje wilt u: \n"))
    if nummer > 12 or nummer < 1:
        print("Dit kluisje bestaat niet")
        file.close
        exit()
    elif nummer not in kluisjes:
        print("Dit kluisje is al bezet.")
        file.close
        exit()


    wachtwoord =  str(input("Voer een code in van 4 tekens: \n"))

    if len(wachtwoord) < 4:
        print("Uw wachtwoord is te klein")
    elif len(wachtwoord) > 4:
        print("Uw wachtwoord is te groot")
    elif wachtwoord in wachtwoorden:
        print("U kunt dit wachtwoord niet gebruiken, pak een nieuwe")
    else:
        file.read()
        file.write(str(nummer) + ";" + wachtwoord + "\n" )
        kluisjes.remove(nummer)
        print("Kluisje", nummer,"is nu van u." )

if keuze == 3:

    select = ((input("Vul hier uw kluisnummer in: ")))
    if select in gebruikers:
        kluisIndex = gebruikers.index(select)
    else:
        print("Deze kluis is al open")
    ww = (str(input("Voer hier uw wachtwoord in: ")))
    if ww in wachtwoorden:

        wachtwoordIndex = wachtwoorden.index(ww)
    else:
        print("Dit wachtwoord is incorrect")


    if kluisIndex == wachtwoordIndex:
        print("Kluis", select, "is nu geopent")

    else:
        print("Het in gevoerde wachtwoord voor kluis", select, "is incorrect")
        file.close
        exit()



if keuze == 4:



    select = ((input("Vul hier uw kluisnummer in: ")))
    if str(select) in gebruikers:
        kluisIndex = gebruikers.index(select)

    else:
        print("Deze kluis is al vrij")
        exit()

    ww = (str(input("Voer hier uw wachtwoord in: ")))
    if str(ww) in wachtwoorden:
        wachtwoordIndex = wachtwoorden.index(ww)
    else:

        print("Het ingevoerde wachtwoord is onjuist")
        exit()
    if kluisIndex == wachtwoordIndex:
            print("Kluisje: ", select, " is nu vrij! Bedankt voor het gebruiken van onze kluizen!")
            select = str(select)
            gegevens.remove((select + ";" + ww))

            if gegevens == []:
                file.truncate(0)

            else:
                for i in gegevens:
                    a = i + "\n"

                file.truncate(0)
                file.write(a)

    else:
        print("Het in gevoerde wachtwoord voor kluis", select, "is incorrect")

        file.close()

        exit()
else:

    file.close()