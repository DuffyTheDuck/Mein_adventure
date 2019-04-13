import sys, time, os
import pickle


intro_text = """
Willkommen zu diesem unglaublichen Spiel
wir werden noch sehen wohin uns die Reise
führen wird, ich wünsche viel Glück
"""


def spiel_intro():
    for buchstabe in intro_text:
        sys.stdout.write(buchstabe)
        sys.stdout.flush()
        time.sleep(0.1)


def erstelle_spieler():
    while True:
        print("Bitte gib den Namen ein den du im Spiel benutzen möchtest.")
        spielername = input(">: ")
        print(f"ist {spielername} der Name den du nutzen möchtest? ( ja / nein )?")
        frage = ""
        while frage not in ["ja", "nein"]:
            frage = input(">: ")
            if frage == "ja":
                return spielername
            else:
                continue

def lade_spiel():
    os.system("cls")
    with open("./spielstand/spieler", "rb") as f:
        spieler = pickle.load(f)
        print("Spielerprofil geladen")
        time.sleep(2)
    with open("./spielstand/welt", "rb") as f:
        spielwelt = pickle.load(f)
        print("Spielewelt wurde geladen")
        time.sleep(2)
    with open("./spielstand/geschaefte", "rb") as f:
        geschaefte = pickle.load(f)
        print("Geschäfte wurden geladen")
    return spieler, spielwelt, geschaefte

def laden_oder_neu():
    entscheidung = "nein"
    if os.path.exists("./spielstand/spieler") and os.path.exists("./spielstand/welt"):
        print("Es gibt ein gespeichertes Spiel, soll es geladen werden oder möchtest du ein neues Spiel starten?")
        frage = ""
        while frage.lower() not in ["laden", "neu"]:
            frage = input("( laden / neu ) >:")
        if frage == "laden":
            entscheidung = "ja"
            return entscheidung
        else:
            return entscheidung
    else:
        return entscheidung
