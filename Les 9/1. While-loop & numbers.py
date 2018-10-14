nummers = ()
uitkomst = 0
aantal = 0
while nummers != 0:
    nummers = int(input("Voer een getal in: "))
    uitkomst = uitkomst + nummers
    if nummers != 0:
        aantal = aantal + 1

print("Er zijn", aantal, "nummers ingevoerd en de optel som is", uitkomst)