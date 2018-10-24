from tkinter import *
import xmltodict
import requests



root = Tk()
label1 = Label(master=root,text="1",height=2)
label1.pack(padx=10, pady=10)
label2 = Label(master=root,text="2",height=2)
label2.pack(padx=10, pady=10)
label3= Label(master=root,text="3",height=2)
label3.pack(padx=10, pady=10)
label4 = Label(master=root,text="4",height=2)
label4.pack()
label5 = Label(master=root,text="5",height=2)
label5.pack(padx=10, pady=10)



def Click():
    keuze = str(entry.get())
    print(keuze)
    auth_details = ('peter.schenkels@student.hu.nl', 'opiHlhav9xP3s-YQEj1FBFOLU7feW1278XEAVV3l7L-vsZcou_L-7w')
    api_url = 'http://webservices.ns.nl/ns-api-avt?station=' + keuze

    response = requests.get(api_url, auth=auth_details)
    with open('vertrektijden.xml', 'w') as myXMLFile:
        myXMLFile.write(response.text)

    vertrekXML = xmltodict.parse(response.text)

    def processXML(Filename):
        with open(Filename) as myXMLFile:
            filestring = myXMLFile.read()
            xmldictionary = xmltodict.parse(filestring)
            return xmldictionary

    stationsdict = processXML('vertrektijden.xml')
    stations = stationsdict['ActueleVertrekTijden']['VertrekkendeTrein']
    t1 = (dict(stations[0])["VertrekTijd"][11:16], dict(stations[0])["EindBestemming"])
    t2 = (dict(stations[1])["VertrekTijd"][11:16], dict(stations[1])["EindBestemming"])
    t3 = (dict(stations[2])["VertrekTijd"][11:16], dict(stations[2])["EindBestemming"])
    t4 = (dict(stations[3])["VertrekTijd"][11:16], dict(stations[3])["EindBestemming"])
    t5 = (dict(stations[4])["VertrekTijd"][11:16], dict(stations[4])["EindBestemming"])
    label1["text"] = t1
    label2["text"] = t2
    label3["text"] = t3
    label4["text"] = t4
    label5["text"] = t5
    return
button = Button(master=root, text='Druk hier', command=Click)
button.pack(pady=10)
label6 = Label(master=root,text="Voer hier uw beginstation in",height=2)
label6.pack()
entry = Entry(master=root)
entry.pack()






root.mainloop()