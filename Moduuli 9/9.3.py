class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus = 0, kuljettumatka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettumatka = kuljettumatka

    def kiihdyta(self, nopeudenmuutos):
        if nopeudenmuutos + self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif nopeudenmuutos + self.nopeus <= 0:
            self.nopeus = 0
        else:
            self.nopeus = nopeudenmuutos + self.nopeus

    def kulje(self, aika):
        self.kuljettumatka = self.kuljettumatka + (aika * self.nopeus)
        print(f"Auto kulki {aika * self.nopeus} km. Matkaa on kuljettu yhteensä {self.kuljettumatka} km.")

auto = Auto("ABC-123", 142)

auto.kuljettumatka = 2000
auto.nopeus = 60
auto.kulje(1.5)
