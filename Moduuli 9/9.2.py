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
        #self.nopeus += muutos
        #if self.nopeus > self.huippunopeus:
            #self.nopeus = self.huippunopeus
        #if self.nopeus < 0:
            #self.nopeus = 0

auto = Auto("ABC-123", 142)

auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)
print(f"Auton nopeus on nyt {auto.nopeus} km/h")
auto.kiihdyta(-200)
print("HÄTÄ JARRUTUS!!")
print(f"Hätäjarrutuksen jälkeinen nopeutesi on {auto.nopeus} km/h")