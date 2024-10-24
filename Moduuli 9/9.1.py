class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus = 0, kuljettumatka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettumatka = kuljettumatka

auto = Auto("ABC-123", 142)

#print(f"Auto rekkarilla {auto.rekisteritunnus:s} kykenee ajamaan max {auto.huippunopeus:d} km/h.")

print(f"Auton ominaisuudet ovat seuraavat:"
      f"\nRekisteritunnus {auto.rekisteritunnus:s}"
      f"\nAuton huippunopeus {auto.huippunopeus:d} km/h"
      f"\nTämän hetkinen nopeus {auto.nopeus:d} km/h"
      f"\nKuljettu matka {auto.kuljettumatka:d} km")