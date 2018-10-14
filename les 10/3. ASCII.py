def code(invoerstring):
    nieuw = ""
    for char in invoerstring:
        let = ord(char) + 3
        let = chr(let)
        nieuw = (nieuw + let)
    print(nieuw)

gebruiker = input("Gebruiker: ")
beginstation =  input("Beginstation: ")
eindstation =  input('Eindstation: ')
codes = (gebruiker + beginstation + eindstation)
code(codes)