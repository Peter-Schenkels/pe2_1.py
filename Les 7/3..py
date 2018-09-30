file = open("Kaartnummers.txt")

lijst = []
for i in file.readlines():
    lijst.append(i.split(","))

hoogstenummer = max(lijst)
file.close()
print("Deze file telt", len(lijst), ' regels', "\n","Het hoogste getal is:", hoogstenummer[0], 'en dat staat op regel.', str(lijst.index(hoogstenummer) + 1))