def seizoen(maand):
    if maand in [12, 1, 2]:
         print("Winter")
    elif maand in [3, 4, 5]:
        print("lente")
    elif maand in [6, 7, 8]:
        print("Zomer")
    elif maand in [9, 10, 11]:
        print("Herfst")
    else:
        print("Bestaat niet")



seizoen(int(input("Welke maand nummer: ")))