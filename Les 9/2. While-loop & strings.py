woord = ""

while len(woord) != 4:
    woord = input("Geef een string van vier letters: ")
    print(woord)
    if len(woord) == 4:
        break
print("Inlezen van correcte string:", woord, "is geslaagd")