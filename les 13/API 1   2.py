import requests
import xmltodict


while True:

        keuze = str(input("Vul hier uw vertrek station in:"))
        auth_details = ('peter.schenkels@student.hu.nl', 'opiHlhav9xP3s-YQEj1FBFOLU7feW1278XEAVV3l7L-vsZcou_L-7w')
        api_url = 'http://webservices.ns.nl/ns-api-avt?station=' + keuze

        response = requests.get(api_url, auth=auth_details)
        with open('vertrektijden.xml', 'w') as myXMLFile:
                myXMLFile.write(response.text)

        vertrekXML = xmltodict.parse(response.text)


        try:

                print('Dit zijn de vertrekkende treinen:')
                for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
                        eindbestemming = vertrek['EindBestemming']
                        soort = vertrek["TreinSoort"]

                        spoorAtt = dict(vertrek["VertrekSpoor"]).get("#text")
                        spoor = spoorAtt.get("#text")

                        vertrektijd = vertrek['VertrekTijd']

                        vertrektijd = vertrektijd[11:16]


                        print('Om ' + vertrektijd + ' vertrekt een trein naar ' + eindbestemming + "\n" + "Soort trein", soort, "op spoor", spoor)
        except:
                print("Ingevoerde station is onjuist of bestaat niet")