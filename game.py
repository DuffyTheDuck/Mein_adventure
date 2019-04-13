from player import Spieler
from gegner import Gegner
from welt import karte
from eingabe import eingabe_programm
from kartenansicht import *
from intro import *
from einkauf import shops


def hauptprogramm():
    # Mit während das spiel läuft erstellen wir eine Endlosschleife
    # die unser Spiel am laufen hält, bis ein von uns gewählter Zustand
    # erreicht ist
    while spiel_laeuft:
        ## Wenn im eingabe_programm ein befehl und ein objekt
        ## zugeordnet werden konnten, werden sie hier mit dem
        ## return befehl an die Variablen befehl und objekt
        ## übergeben
        befehl, objekt = eingabe_programm()

        if befehl == "gehen":
            # Wenn der Variablen "gehen" übergeben wurde, starten wir die
            # Funktion bewege_spieler aus der Klasse Spieler und übergeben
            # dieser die zwei Werte objekt(Richtung) und spielwelt
            if objekt.lower() == "einkaufen":
                os.system("cls")
                spieler.einkaufen(spielwelt, geschaefte)
            else:
                spieler.bewege_spieler(objekt, spielwelt)
                if spielwelt[spieler.ort]["gibt_gegner"]:
                    gegner = Gegner()
                    gegner.erstelle_gegner(spieler, spielwelt)
                    antwort = spieler.gegner_erwarten(gegner)
                    if antwort == "flucht":
                        spieler.bewege_spieler(antwort, spielwelt)
                    else:
                        antwort = spieler.nimm_waffe()
                        spieler.kampf(gegner, spielwelt)

        elif befehl == "nehmen":
            # Wenn der Variablen "nehmen" übergeben wurde, starten wir die
            # Funktion nimm_objekt aus der Klasse Spieler und übergeben
            # dieser die zwei Werte objekt(Objekt) und spielwelt
            spieler.nimm_objekt(objekt, spielwelt)
        elif befehl == "untersuche":
            spieler.untersuche_objekt(objekt, spielwelt)

        elif befehl == "zeige" and objekt.lower() == "karte":
            os.system("cls")
            finde_spielerposition(spieler.ort)

        elif befehl == "speicher" and objekt.lower() in ["spiel", "game"]:
            with open("./spielstand/spieler", "wb") as f:
                pickle.dump(spieler, f)
            print("Deine Fortschritte wurden gespeichert...")
            time.sleep(2)
            with open("./spielstand/welt", "wb") as f:
                pickle.dump(spielwelt, f)
            print("Die Spielwelt wurde gespeichert...")
            time.sleep(1)
            with open("./spielstand/geschaefte", "wb") as f:
                pickle.dump(geschaefte, f)
            print("Die Geschäfte wurden gesichert...")





if __name__ == "__main__":
    #spiel_intro()
    entscheidung = laden_oder_neu()
    if entscheidung == "nein":
        spieler = Spieler()
        spieler.name = erstelle_spieler()
        spielwelt = karte
        geschaefte = shops
    else:
        spieler, spielwelt = lade_spiel()

    ort = spielwelt[spieler.ort]["name"]
    beschreibung = spielwelt[spieler.ort]["beschreibung"]
    print(f"Du befindest dich {ort}")
    print(f"{beschreibung}")
    spieler.erkenne_objekte(spielwelt)
    # Der Variablen spiel_laeuft wird der Wahrheitswert übergeben
    spiel_laeuft = True
    # Hier wird das Hauptprogramm mit Endlosschleife gestartet
    hauptprogramm()
