groen = {"Best", "Beukenlaan", "Helmond 't Hout", "Helmond", "Helmond Brouwhuis", "Deurne"}
bruin = {"Best", "Beukenlaan", "Geldrop", "Heeze", "Weert"}
print(bruin.intersection(groen))
print(bruin.difference(groen))
print(bruin.difference(groen), groen.difference(bruin), bruin.intersection(groen))
