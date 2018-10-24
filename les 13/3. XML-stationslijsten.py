import os
from xml.etree import ElementTree
file_name = "traject.xml"
file = os.path.join(file_name)
dom = ElementTree.parse(file)
station = dom.findall('Station')
syn = []

for c in station:

    type = c.find("Type").text
    code = c.find("Code").text


    print("{} {}".format(code, type))

print("\n")

for c in station:

    code = c.find("Code").text


    if c.find("Synoniemen").text != None:
        syn = []
        for i in c.findall("Synoniemen/Synoniem"):
            syn.append(i.text)

        print("{} {}".format(code, syn))
    else:
        syn = ""

print("\n")

for c in station:

    type = c.find("Type").text
    code = c.find("Code").text

    if c.find("Namen").text != None:
        naam = ""
        for i in c.findall("Namen/Lang"):
            naam = i.text

        print("{} {}".format(code, naam))
    else:
        naam = ""
