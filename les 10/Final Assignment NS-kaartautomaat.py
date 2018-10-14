
def inlezen_beginstation(stations):
    correct = False
    while correct == False:
        Station = input("Schrijf hier uw begin station: ")
        if Station in stations:
            correct = True
        else:
            print("Dit station zit niet in dit traject.")

    return Station


def inlezen_eindstation(stations, beginstation):
    correct = False
    while correct == False:
        Station = input("Schrijf hier uw eind station: ")
        if Station in stations and stations.index(beginstation) < stations.index(Station):
            correct = True
        elif Station not in stations:
            print("Dit station zit niet in dit traject.")
        else:
            print("Error.")
    return Station

def omroepen_reis(stations, beginstation, eindstation):
    tussenliggendestations = []
    stationIndex = (stations.index(eindstation) - stations.index(beginstation))
    print("Dit is uw begin station:", beginstation, "\n", "rangnummer:", stations.index(beginstation), "\n")
    print("Dit is uw eind station:", eindstation, "\n", "rangnummer:", stations.index(eindstation), "\n")
    print("De afstand bedraagt", stations.index(eindstation) - stations.index(beginstation), 'Stations', "\n")
    print("De prijs van het kaartje bedraagt €", 5 * stationIndex , "\n")
    print("Jij stapt in de trein in: ", beginstation, "\n")
    print("Jij stapt uit de trein in: ", eindstation, "\n")
    for i in range(stations.index(beginstation) + 1, stations.index(eindstation )):
        tussenliggendestations.append(stations[i])
    if len(tussenliggendestations) > 0:
        print("Je tussen liggende stations zijn:", tussenliggendestations)




stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', '’s-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)


