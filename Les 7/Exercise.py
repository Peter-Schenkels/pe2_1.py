#Defenitions

def BMI (Lengte, gewicht):
    a = (gewicht * 703/ Lengte**2)
    if 18.5 > a:
        print("Je hebt ondergewicht")
    elif 25.0 < a:
        print("Je hebt overgweicht")
    else:
        print("Je bent gezond")

#Inputs

L = int(input("Wat is je lengte in inches? :"))
G = int(input("Wat is je gewicht in ponden? :"))


#Executions

BMI(L,G)



