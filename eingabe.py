from wortschatz import woerter


def eingabe_programm():
    while True:
        temp_befehl = []
        temp_objekt = []
        eingabe = input("Deine Eingabe >: ")
        text = eingabe.lower().strip().split()
        if len(text) == 0:
            continue
        for wort in text:
            for schluessel, wert in woerter["befehle"].items():
                if wort in wert:
                    temp_befehl.append(schluessel)
            for schluessel, wert in woerter["richtungen"].items():
                if wort in wert:
                    temp_objekt.append(wort)

            try:
                if wort in woerter["alle_woerter"]:
                    temp_objekt.append(wort)
                else:
                    pass
            except Exception as fehler:
                pass

        if len(temp_befehl) > 1:
            for befehl in temp_befehl:
                print(f"{befehl} als Befehl erkannt")
            print("Spezifiziere deine Eingabe!")

        elif len(temp_objekt) > 1:
            try:
                for objekt in temp_objekt:
                    print(f"==> {temp_befehl[0]} | {objekt} <==")
                print("Triff eine Auswahl")

            except Exception as f:
                print("Kein Befehl erkannt!")
        elif len(temp_objekt) == 0 and len(temp_befehl) > 0:
            print(f"Was möchtest du mit {temp_befehl[0]} erreichen?")

        elif len(temp_befehl) == 0 and len(temp_objekt) > 0:
            print(f"Was soll mit {temp_objekt[0]} geschehen?")

        elif len(temp_befehl) == 0 and len(temp_objekt) == 0:
            print("Deine Eingabe ergibt keinen Sinn!")

        else:
            try:
                befehl = temp_befehl[0]
                objekt = temp_objekt[0]
                return befehl, objekt

            except Exception as e:
                print("Deine Eingabe ist unverständlich!")