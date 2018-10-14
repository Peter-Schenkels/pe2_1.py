file = open("dict.txt")
x = 4
def ticker(filename):
    set = {}
    temp = []
    for i in filename.readlines():
        temp.extend(i.split(':'))
        set[temp[0]] = temp[1]
        temp = []

    return set



set = ticker(file)


while x != 0:
    x = int(input("Wat wilt u doen? \n Kies 1 om een ticker symbool in te voeren: \n Kies 2 om een bedrijfsnaam in te voeren: \n Kies 0 om te stopppen: \n"))
    if x == 1:
        tckr = (input("Voer hier het ticker symbool in: \n"))
        for key, value in set.items():
            if set[key] == tckr:
                print(key)




    if x == 2:
        Bedrijfsnaam = (input("Voer hier het bedrijfsnaam in: \n"))

        print(set[Bedrijfsnaam])
