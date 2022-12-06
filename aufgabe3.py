def getNummer_gericht():
    nummer_gericht = 0
    with open("Speisekarte_CafeDerksen.txt", "r") as datei:
        content = datei.read()
        contentList = content.split("\n")
        for content in contentList:
            nummer_gericht += 1

    with open("Speisekarte_CafeDerksen.txt", "r") as datei:
        content = datei.read()
        contentList = content.split("\n")
    for content in contentList:
        nummer_gericht += 1
        if nummer_gericht > 1:
            nummer_gericht -= 1
    if nummer_gericht > 1:
        nummer_gericht -= 1
    return nummer_gericht

def getSpeisekarte():
    speisekarte = []
    with open("Speisekarte_CafeDerksen.txt", "r") as datei:
        content = datei.read()
        contentList = content.split("\n")

        for content in contentList:
            # von 0:2 weil die ersten beiden Zeichen die Zahl + Leerzeichen sind
            speisekarte = speisekarte + [content.strip(content[0:2])]

        for content in speisekarte:
            if content == "":
                speisekarte.remove(content)

        # Da ich in meiner Textdatei oben Speisekarte stehen habe, wird das oben als Variable mitgezählt und erhöht die Nummer. Insofern die Datei vorher beschrieben wurde, wird das hier korrigiert.
        for content in speisekarte:
            if content == "eisekarte":
                speisekarte.remove(content)
        return speisekarte


def getGerichteliste():
    getSpeisekarte()
    gerichteliste = {}
    for item in speisekarte:
        gerichteliste.update({item.split(": ")[0]: int(item.split(": ")[1])})
    return gerichteliste

def gerichtelisteAnzeigen(gerichteliste):
    while True:
        print(gerichteliste)
        print("\nMit einer leeren Eingabe gelangen Sie zurück ins Hauptmenü.")
        back = input()
        if back == "":
            return

def speisekarteAnzeigen():
    while True:
        with open("Speisekarte_CafeDerksen.txt", "r") as datei:
            content = datei.read()
            print("\n" + content + "\n")
        print("Mit einer leeren Eingabe gelangen Sie zurück ins Hauptmenü.")
        back = input()
        if back == "":
            return


def gerichtHinzufuegen(nummer_gericht, gerichteliste, speisekarte):
    speisekarte = getSpeisekarte()
    nummer_gericht = getNummer_gericht()
    while True:
        print("Mit einer leeren Eingabe gelangen Sie zurück ins Hauptmenü.")
        print("Bitte geben Sie das Gericht ein, welches Sie hinzufügen möchten: ")

        gericht = input()
        if gericht == "":
            return nummer_gericht, gerichteliste, speisekarte
        print("Bitte geben Sie den Preis des Gerichts in Cent ein: ")
        exception = True
        while exception:
            preis = input()
            if preis == "":
                return nummer_gericht, gerichteliste, speisekarte
            try:
                int(preis)
            except ValueError:
                print("Bitte schreiben Sie eine Zahl")
            else:
                exception = False

        gerichteliste[gericht] = int(preis)
        speisekarte = speisekarte + [gericht + ": " + str(preis)]

        with open("Speisekarte_CafeDerksen.txt", "a") as datei:
            if nummer_gericht == 1:
                datei.write("Speisekarte\n \n" + str(nummer_gericht) + " " + gericht + ": " + str(preis))
                nummer_gericht += 1
                return nummer_gericht, gerichteliste, speisekarte
            else:
                datei.write("\n" + str(nummer_gericht) + " " + gericht + ": " + str(preis))
                nummer_gericht += 1
                return nummer_gericht, gerichteliste, speisekarte

def gerichtLoeschen(nummer_gericht, gerichteliste, speisekarte):
    speisekarte = getSpeisekarte()
    nummer_gericht = getNummer_gericht()
    while True:
        if speisekarte.__len__() < 1:
            print("Die Speisekarte ist zurzeit leer.\n")
            return nummer_gericht, gerichteliste, speisekarte
        with open("Speisekarte_CafeDerksen.txt", "r") as datei:
            content = datei.read()
            print(content)

        print("\nDurch eine leere Eingabe gelangen Sie ins Hauptmenü zurück.")
        print("Schreiben Sie die Nummer des Gerichts, welches Sie löschen möchten: ")
        exception = True
        while exception:
            zahl = input()
            if zahl == "":
                return nummer_gericht, gerichteliste, speisekarte
            try:
                zahl = int(zahl)
            except ValueError:
                print("Bitte schreiben Sie eine Zahl")
            else:
                if zahl > speisekarte.__len__() or zahl <= 0:
                    print("Bitte schreiben Sie eine Zahl von 1 bis " + str(speisekarte.__len__()))
                else:
                    exception = False

        nummer_gericht -= 1
        del gerichteliste[speisekarte[zahl - 1].split(": ")[0]]
        speisekarte.remove(speisekarte[zahl - 1])

        with open("Speisekarte_CafeDerksen.txt", "w") as datei:
            index = 1
            for content in speisekarte:
                if index == 1:
                    datei.write("Speisekarte\n \n" + str(index) + " " + content)
                    index += 1
                else:
                    datei.write("\n" + str(index) + " " + content)
                    index += 1
            print("\nGeupdatete Gerichteliste:")
            print(gerichteliste)
            print()
            return nummer_gericht, gerichteliste, speisekarte



speisekarte = getSpeisekarte()
index = 0
nummer_gericht = 0
gerichteliste = getGerichteliste()



on = True
while on:
    print(
        "Hauptmenü: \n a = Gerichteliste anzeigen lassen \n b = Speisekarte anzeigen lassen \n e = Programm beenden \n n = Gericht hinzufügen \n 1 = Gericht löschen \n")
    user_input = input()


    if user_input == "a":
        gerichtelisteAnzeigen(gerichteliste)

    if user_input == "b":
        speisekarteAnzeigen()

    if user_input == "e":
        on = False

    if user_input == "n":
        gerichtHinzufuegen(nummer_gericht, gerichteliste, speisekarte)

    if user_input == "1":
        gerichtLoeschen(nummer_gericht, gerichteliste, speisekarte)
