def namen(list):
    temp = 0
    temp1 = ''
    set = {}
    for i in list:
        if i != '':
            if i != temp1:
                for name in list:
                    if name == i:
                        temp = temp + 1

                    temp1 = i

            if temp != 0:
                set[i] = temp
            temp = 0


    for key, value in set.items():
        print("Er zijn", set[key], "leerling(en) met de naam", key)

namens = "j"
lists = []
while namens != "":
    namens = input("Volgende naam: ")
    lists.append(namens)

namen(lists)