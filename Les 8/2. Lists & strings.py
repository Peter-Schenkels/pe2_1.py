list = []
list4 = []
listCheck = []
listCount = 0
listWord = ""
words = (input("voer een list in met 10 verschillende strings (Scheid de strings met een komma): "))

listCheck.extend(words.split(","))

if len(listCheck) == 10:
    for i in words:
        if i != "," and  i != " " and i != "\"" and i != "[" and i != "]":
            listCount = listCount + 1
            listWord = listWord + i
        if i == "," and listCount != 4:
            list.append(listWord)
            listWord = ""
            listCount = 0
        if i == "," and listCount == 4:
            list4.append(listWord)
            listWord = ""
            listCount = 0
elif len(listCheck) < 10:
    print("Lijst is te klein")
else:
    print("List is te groot")


print(list)
print(list4)