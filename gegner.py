class Gegner:

    def __init__(self):
        self.name = ""
        self.lebenspunkte = 0
        self.angriffspunkte = 0
        self.gegenstand = {}
        self.am_leben = True

    def erstelle_gegner(self, spieler, spielewelt):
        if spielewelt[spieler.ort]["gibt_gegner"]:
            for schluessel in spielewelt[spieler.ort]["gegner"].keys():
                self.name = spielewelt[spieler.ort]["gegner"][schluessel]["name"]
                self.lebenspunkte = spielewelt[spieler.ort]["gegner"][schluessel]["lebenspunkte"]
                self.angriffspunkte = spielewelt[spieler.ort]["gegner"][schluessel]["angriffspunkte"]
                self.gegenstand = spielewelt[spieler.ort]["gegner"][schluessel]["gegenstand"]

    def __repr__(self):
        return self.name + " mit " + str(self.lebenspunkte) + " Leben und " + str(self.angriffspunkte) + " Angriffspunkten"

    def hole_lebenspunkte(self):
        if self.lebenspunkte > 0:
            return self.lebenspunkte
        else:
            self.am_leben = False
            return self.am_leben
