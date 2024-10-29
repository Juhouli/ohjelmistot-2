class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjailijannimi, sivumaara):
        self.kirjailijannimi = kirjailijannimi
        self.sivumaara = sivumaara
        super().__init__(nimi)

    def tulostatiedot(self):
        print(f"Kirja: {self.nimi}"
              f"\nKirjailija: {self.kirjailijannimi}"
              f"\nSivumäärä: {self.sivumaara}\n")

class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        self.paatoimittaja = paatoimittaja
        super().__init__(nimi)

    def tulostatiedot(self):
        print(f"Lehti {self.nimi}"
              f"\nPäätoimittaja: {self.paatoimittaja}\n")

kirja = Kirja("Hytti n:o 6", "Rosa Liksom", 200)
lehti = Lehti("Aku Ankka", "Aki Hyyppä")

kirja.tulostatiedot()
lehti.tulostatiedot()