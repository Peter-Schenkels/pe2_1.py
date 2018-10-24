temp = []
scores = []
namen = []
datum = []
with open("gamers.csv", "r") as gamers:
    for row in gamers.readlines():
        temp.extend(row.split(";"))
        scores.append(temp[2])
        namen.append(temp[0])
        datum.append(temp[1])
        temp.clear()
    index = scores.index(max(scores))
    print(namen[index], "heeft de hoogste scoren met:", scores[index], "punten! Behaald op:", datum[index])
