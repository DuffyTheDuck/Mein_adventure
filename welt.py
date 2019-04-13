karte = {
    "u1": {
        "key": "u1",
        "name": "Der Anfang",
        "beschreibung": "Du stehst bla bla bla",
        "richtungen": {"osten": "u2", "flucht": None},
        "gibt_gegner": False,
        "gegner": {},
        "gegenstaende": {
            "waffen": {
                "messer": {"name": "messer", "angriffspunkte": 10, "beschreibung": "Ein kleines Messer mit 12 cm Klinge"}
            },
            "gegenstand": {
                "türkarte": {"name": "türkarte", "beschreibung": "Auf der Karte steht der Code 2246"}
            },
            "nahrung": {},
            "getraenk": {}
        },
        "gibt_geschaeft": False
    },
    "u2": {
        "key": "u2",
        "name": "Der zweite Raum",
        "beschreibung": "Hier führt ein Weg nach osten und einer nach westen",
        "richtungen": {"westen": "u1", "osten": "u3", "flucht": "u1"},
        "gibt_gegner": True,
        "gegner": {
            "riesenspinne": {"name": "riesenspinne", "lebenspunkte": 50, "angriffspunkte": 8, "gegenstand": {
                "name": "Gold", "wert": 25
            }}
        },
        "gegenstaende": {},
        "gibt_geschaeft": False

    },
    "u3": {
        "key": "u3",
        "name": "Der dritte Raum",
        "beschreibung": "Das Monster überstanden, ein Weg führt zurück nach Westen und einer nach Süden",
        "richtungen": {"westen": "u2", "süden": "u10"},
        "gibt_gegner": False,
        "gegner": {},
        "gegenstaende": {},
        "gibt_geschaeft": True
    },
    "u10": {
        "key": "u10",
        "name": "Der vierte Raum im Norden geht es zurück",
        "beschreibung": "Weiter testen",
        "richtungen": {"norden": "u3"},
        "gibt_gegner": False,
        "gegner": {},
        "gegenstaende": {},
        "gibt_geschaeft": False
    }
}
