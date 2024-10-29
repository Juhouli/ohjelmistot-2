from random import randint

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

class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankintilavuus):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankintilavuus = bensatankintilavuus

class Kilpailu:
    def __init__(self, kilpailun_nimi, kilpailun_pituus, autot):
        self.kilpailun_nimi = kilpailun_nimi
        self.kilpailun_pituus = kilpailun_pituus
        self.autot = autot
        self.tunteja_kulunut = 0

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kiihdyta(randint(-10,15))
            auto.kulje(1)
        self.tunteja_kulunut +=1


    def kilpailuohi(self):
        for auto in self.autot:
            if auto.kuljettumatka >= self.kilpailun_pituus:
                print(f"Kilpailu on päättynyt. Kilpailun kesto oli {self.tunteja_kulunut} tuntia. Lopputulokset:")
                return True

    def tulostatilanne(self):
        print("Rekisteritunnus   Huippunopeus  Kuljettumatka")
        for i in range(len(self.autot)):
            print(f"{self.autot[i].rekisteritunnus}           {self.autot[i].huippunopeus}           {self.autot[i].kuljettumatka}")

osallistujat = []
osallistujat.append(Sahkoauto("ABC-15 ",180,52.5))
osallistujat.append(Polttomoottoriauto("ACD-123",165,32.3))

kisa = Kilpailu("Testi", 8000, osallistujat)

loppu = False
while kisa.tunteja_kulunut < 3:
    kisa.tunti_kuluu()

#print(osallistujat[0].rekisteritunnus, osallistujat[1].rekisteritunnus)
#print(osallistujat[0].huippunopeus, osallistujat[1].huippunopeus)
#print(osallistujat[0].nopeus, osallistujat[1].nopeus)
#print(osallistujat[0].kuljettumatka, osallistujat[1].kuljettumatka)

kisa.tulostatilanne()

