file = open("Kaartnummers.txt", "r")

for i in file.readlines():
    a = i.split(",")
    print(a[1] + " heeft kaartnummer: " + a[0])

