from config import *
import time
import sys
import os

class Spieler:
    def __init__(self, name=""):
        self.name = name
        self.angriffspunkte = 5
        self.heilungswert = 0
        self.lebenspunkte = 100
        self.gold = 100
        self.ort = "u1"
        self.inventar = inventar
        self.am_leben = True
        self.waffe = ""
        self.waffen_angriffspunkte = 0

    def __repr__(self):
        return "Name: " + self.name + " Lebenspunkte: " + str(self.lebenspunkte)

    def hole_lebenspunkte(self):
        if self.lebenspunkte > 0:
            return self.lebenspunkte
        else:
            self.am_leben = False
            return self.am_leben

    def erkenne_objekte(self, spielwelt):
        print("Von deiner Position aus siehst du:")
        for schluessel in spielwelt[self.ort]["gegenstaende"].keys():
            for unterschluessel in spielwelt[self.ort]["gegenstaende"][schluessel].keys():
                print(f"{unterschluessel}")

    def bewege_spieler(self, richtung, spielewelt):
        if richtung in spielewelt[self.ort]["richtungen"]:
            os.system("cls")
            alter_ort = spielewelt[self.ort]["name"]
            self.ort = spielewelt[self.ort]["richtungen"][richtung]
            name = spielewelt[self.ort]["name"]
            beschreibung = spielewelt[self.ort]["beschreibung"]
            if spielewelt[self.ort]["gibt_gegner"]:
                print(f"Du bewegst dich von {alter_ort} nach {name}")
            else:
                print(f"Du bewegst dich von {alter_ort} nach {name}")
                print(beschreibung)
                self.erkenne_objekte(spielewelt)
            if spielewelt[self.ort]["gibt_geschaeft"] is True:
                print("An diesem Ort gibt es die Möglichkeit einzukaufen.")
                print("Nutze den Befehl gehe einkaufen um sie zu nutzen!!!")
        else:
            print(f"{self.name} in diese Richtung kannst du nicht gehen!")

    def gegner_erwarten(self, gegner):
        print("Hier erwartet dich:")
        print(gegner)
        print("Möchtest du deinem Gegner entgegentreten?")
        frage = ""
        while frage.lower() not in ["kampf", "flucht"]:
            frage = input("(Kampf oder Flucht) >: ")
        return frage

    def nimm_objekt(self, objekt, spielewelt):
        for schluessel in spielewelt[self.ort]["gegenstaende"].keys():
            for unterschluessel, wert in spielewelt[self.ort]["gegenstaende"][schluessel].items():
                if objekt == unterschluessel:
                    self.inventar[schluessel][unterschluessel] = wert
                    print(f"{objekt} wurde deinem Inventar hinzugefügt.")
                    del spielewelt[self.ort]["gegenstaende"][schluessel][unterschluessel]
                    return

        print(f"{objekt} gibt es hier nicht!")

    def untersuche_objekt(self, objekt, spielewelt):
        for schluessel in spielewelt[self.ort]["gegenstaende"].keys():
            for unterschluessel, wert in spielewelt[self.ort]["gegenstaende"][schluessel].items():
                if objekt == unterschluessel:
                    print(spielewelt[self.ort]["gegenstaende"][schluessel][unterschluessel]["beschreibung"])
                    return
        for eintrag in self.inventar.keys():
            if objekt.lower() in self.inventar[eintrag]:
                print(self.inventar[eintrag][objekt]["beschreibung"])
                return
        print(f"{objekt} kann ich nicht untersuchen!")

    def nimm_waffe(self):
        waffen = []
        self.waffe = ""
        self.waffen_angriffspunkte = 0
        print("Welche Waffe möchtest du benutzen?")
        print("Diese Waffen stehen dir zur Verfügung:")
        if len(self.inventar["waffen"]) < 1:
            print("Du hast keine Waffe im Inventar!")
            print(f"{self.name} du mußt mit blossen Händen kämpfen!")
            frage = ""
            while frage.lower() not in ["ja", "nein"]:
                frage = input("( ja oder nein ) >: ")
            return frage
        else:
            for waffe, details in self.inventar["waffen"].items():
                waffen.append(waffe)
                atp = str(self.inventar["waffen"][waffe]["angriffspunkte"])
                print(f"Waffe: {waffe} mit {atp} Angriffspunkten")
            while self.waffe not in waffen:
                self.waffe = input("Wähle deine Waffe >: ")
            self.waffen_angriffspunkte = self.inventar["waffen"][self.waffe]["angriffspunkte"]
            print(f"{self.name} du hast dich für {self.waffe} mit {str(self.waffen_angriffspunkte)} Angriffspunkten entschieden.")

    def kampf(self, gegner, spielewelt):
        os.system("cls")
        if len(self.waffe) > 0:
            schaden = self.waffen_angriffspunkte
        else:
            schaden = self.angriffspunkte
        while self.am_leben is True:
            gegner.lebenspunkte -= schaden
            print(f"Du greifst {gegner.name} an und verursachst {str(schaden)} Schaden")
            print(f"{gegner.name} hat jetzt noch {str(gegner.lebenspunkte)} übrig!\n")
            time.sleep(2)
            self.lebenspunkte -= gegner.angriffspunkte
            print(f"{gegner.name} greift dich an und verursacht {str(gegner.angriffspunkte)} Schaden")
            print(f"{self.name} du hast jetzt noch {str(self.lebenspunkte)} übrig\n")
            time.sleep(2)
            gegner.hole_lebenspunkte()
            self.hole_lebenspunkte()
            if not self.am_leben:
                print(f"Schade {self.name} das hast du leider nicht überlebt vielleicht hast du nächstes mal mehr Glück")
                sys.exit(0)
            elif gegner.am_leben is False:
                os.system("cls")
                prämie = spielewelt[self.ort]["gegner"][gegner.name]["gegenstand"]["wert"]
                self.gold += prämie
                print(f"Super du hast {gegner.name} besiegt!!!")
                print(f"Du erhälst für deinen Sieg {str(prämie)} Gold du hast jetzt {str(self.gold)} Gold")
                spielewelt[self.ort]["gibt_gegner"] = False
                print(spielewelt[self.ort]["name"])
                print(spielewelt[self.ort]["beschreibung"])
                return

    def einkaufen(self, spielwelt, geschaefte):
        location = str(spielwelt[self.ort]["key"])
        besitzer = str(geschaefte[location]["besitzer"])
        print(f"Schönen guten Tag mein Name ist {besitzer}\n")
        while True:
            for schluessel in geschaefte[self.ort]["gegenstaende"].keys():
                for unterschluessel, wert in geschaefte[self.ort]["gegenstaende"][schluessel].items():
                    menge = geschaefte[self.ort]["gegenstaende"][schluessel][unterschluessel]["menge"]
                    kosten = geschaefte[self.ort]["gegenstaende"][schluessel][unterschluessel]["kosten"]
                    print(f"Es gibt noch {str(menge)} : {unterschluessel} zum Preis von {str(kosten)}")
            gruppe = ""
            objekt = ""
            erfüllt = False
            while not erfüllt:
                objekt_richtig = False
                print("Was möchten sie kaufen?")
                kaufwunsch = input(">: ")
                for schluessel in geschaefte[self.ort]["gegenstaende"].keys():
                    for unterschluessel, wert in geschaefte[self.ort]["gegenstaende"][schluessel].items():
                        if kaufwunsch == unterschluessel:
                            objekt_richtig = True
                            objekt = unterschluessel
                            gruppe = schluessel
                if objekt_richtig == True:
                    if geschaefte[self.ort]["gegenstaende"][gruppe][objekt]["menge"] > 0:
                        if self.gold > geschaefte[self.ort]["gegenstaende"][gruppe][objekt]["kosten"]:
                            self.gold -= geschaefte[self.ort]["gegenstaende"][gruppe][objekt]["kosten"]
                            self.inventar[gruppe][objekt] = geschaefte[self.ort]["gegenstaende"][gruppe]
                            geschaefte[self.ort]["gegenstaende"][gruppe][objekt]["menge"] -= 1
                            objekt_richtig = True
                            print(f"{objekt} wurde deinem Inventar hinzugefügt.")
                        elif self.gold < geschaefte[self.ort]["gegenstaende"][gruppe][objekt]["kosten"]:
                            print(f"{self.name} das kannst du dir nicht leisten, du hast nu noch{str(self.gold)} Gold zur Verfügung")
                    elif geschaefte[self.ort]["gegenstaende"][gruppe][objekt]["menge"] < 1:
                        print(f"{kaufwunsch}, haben wir leider nicht mehr!")
                        continue
                else:
                    print(f"{kaufwunsch}, so etwas führen wir hier nicht!")
                    continue
                frage = ""
                while frage.lower() not in ["ja", "nein"]:
                    print("Möchten sie noch etwas kaufen?")
                    frage = input("( ja / nein ) >: ")
                if frage == "ja":
                    continue
                else:
                    os.system("cls")
                    erfüllt = True


            return