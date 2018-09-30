import datetime
naam = "Peter"


def aanvullen(naam):
    today = datetime.datetime.today()
    s = today.strftime('%a %d %b %Y, %H:%M:%S')
    file = open("Hardlopers.txt", "a")
    a = ("{}, {}".format(s, naam))
    a = str(a)
    file.write('\n')
    file.write(a)


aanvullen(naam)
