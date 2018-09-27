


def new_password (oldpassword, newpassword):

    check = 1
    for x in newpassword:
        if x in ("0123456789"):
            check = 2

    if len(newpassword) >= 6 and check == 2 and newpassword != oldpassword:
        print("True")
    else:
        print("false")

a = ("Jeutje2")
b = input("Voeg hier je nieuwe wachtwoord in:")
new_password(a, b)