def kwadraten_som(grondgetallen):
    y = 0
    for x in grondgetallen:
        if x >= 0:
          y = y + x * x

    print(y)


kwadraten_som([1, 2, -3, 12])