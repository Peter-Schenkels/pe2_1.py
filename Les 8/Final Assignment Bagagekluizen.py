file = open("Kluissleutels.txt", "r+")
keuze = int(input("1: Ik wil weten hoeveel kluizen nog vrij zijn \n 2: Ik wil een nieuwe kluis  \n 3: Ik wil even iets uit mijn kluis halen  \n 4: Ik geef mijn kluis terug \n"))

gegevens = []
kluisjes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
a = ""

for i in file.read():
    a = a + i

gegevens.append(a.split(";"))2

print(gegevens)
for i in gegevens:
    print(i)
    if len(i) <= 2:

        kluisjes.remove(int(i))

if keuze == 1:
    kluisjesTemp = 12

    for i in file.readlines():
        kluisjesTemp = kluisjesTemp - 1

    print(kluisjesTemp)

elif keuze == 2:



    print("dit zijn alle beschikbare kluisjes: ", kluisjes)
    nummer =  eval(input("Welk kluisje wilt u: \n"))
    if nummer > 12 or nummer < 1:
        print("Dit kluisje bestaat niet")
        (exit)



    wachtwoord =  str(input("Voer een code in van 4 tekens: \n"))

    if len(wachtwoord) != 4:
        print("Uw wachtwoord is te klein")
    else:
        file.read()
        file.write(str(nummer) + ";" + wachtwoord + "\n" )
        kluisjes.remove(nummer)