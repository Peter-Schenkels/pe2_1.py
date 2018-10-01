list = []
invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
list = invoer.split("-")
a = []
for i in list:
    i = int(i)
    a.append(i)

a.sort()

print("Gesorteerde lijst van ints: ", a)
print("Het kleinste getal van de lijst is: ", min(list), " en het grootste getal is: ", max(list))
print("Het aantal getallen: ", len(a), "Optel som van alle getallen: ", sum(a))
gemiddelde = sum(a) / len(list)
print("Gemiddelde van alle getallen: ", gemiddelde )
