from operator import truediv
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


class Kilpailu:
    def __init__(self, kilpailun_nimi, kilpailun_pituus, autot):
        self.kilpailun_nimi = kilpailun_nimi
        self.kilpailun_pituus = kilpailun_pituus
        self.autot = autot
        self.tunteja_kulunut = 0

    def tunti_kuluu(self):
        if self.tunteja_kulunut == 0:
            print(f"\nTervetuloa seuraavaan vuoden 2024 kilpailua nimeltä {self.kilpailun_nimi}! Tänä vuonna {len(self.autot)} hurjapäätä on osallistunut kisaan."
                  f"\nTätä rallia kaahataan, kunnes joku kisaajista on saavuttanut {self.kilpailun_pituus}km mitan jollain tunnin välein olevalla mittauspisteellä."
                  f"\nToivottavasti pakkasitte evästä ja kahvia!")
            print("\nPidemmittä puheitta, aloitetaan itse kisa!"
                  "\nPaikoillanne"
                  "\nValmiit"
                  "\nKAASUA!"
                  "\n... ainiin! Makkaraa ja mehua on tarjolla kiskalla!\n")
        for auto in self.autot:
            auto.kiihdyta(randint(-10,15))
            auto.kulje(1)
        self.tunteja_kulunut +=1
        if self.tunteja_kulunut % 10 == 0:
            print(f"Kilpailu on kestänyt {self.tunteja_kulunut} tuntia. Tilannekatsaus:")
            kisa.tulostatilanne()
            print("\n")


    def kilpailuohi(self):
        for auto in self.autot:
            if auto.kuljettumatka >= self.kilpailun_pituus:
                print(f"Kilpailu on päättynyt. Kilpailun kesto oli {self.tunteja_kulunut} tuntia. Lopputulokset:")
                return True

    def tulostatilanne(self):
        print("Rekisteritunnus  Huippunopeus  Nopeus  Kuljettumatka")
        autot = self.autot
        if len(autot) < 9:
            for i in autot:
                print(
                    f"{autot[i].rekisteritunnus}            {autot[i].huippunopeus}           {autot[i].nopeus}     {autot[i].kuljettumatka}")
        elif len(autot) >= 9 and len(autot) <= 99:
            for i in range(0, 9):
                print(
                    f"{autot[i].rekisteritunnus}            {autot[i].huippunopeus}           {autot[i].nopeus}     {autot[i].kuljettumatka}")
            for i in range(9, len(autot)):
                print(f"{autot[i].rekisteritunnus}           {autot[i].huippunopeus}           {autot[i].nopeus}     {autot[i].kuljettumatka}")

osallistujat = []
for i in range(0,10):
    osallistujat.append(Auto(f"ABC-{i+1}",randint(100,200)))

kisa = Kilpailu("Suuri romuralli", 8000, osallistujat)

loppu = False
while loppu == False:
    kisa.tunti_kuluu()
    if kisa.kilpailuohi() == True:
        loppu = True

kisa.tulostatilanne()
