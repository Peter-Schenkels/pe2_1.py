bedrag = 4356
try:
    aantal = int(input("Hoeveel personen gaan er mee: "))
    if aantal < 0:
        print("Het getal moet groter dan 0 zijn.")
    print( "Het bedrag per persoon is", bedrag % aantal)
except ZeroDivisionError:
    print("Het ingevulde getal mag geen 0 zijn")
except ValueError:
    print("Het ingevulde getal moet de karakters 0123456789 bevatten.")
except:
    print("Error.")