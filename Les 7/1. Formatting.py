def convert (TC):
      TF = TC * 1.8 + 32
      return TF

def table():
    for i in range(-30, 40, 10):
        print("{}  {}".format(convert(i), i))
print("{}      {}".format("C","F"))
print(table())