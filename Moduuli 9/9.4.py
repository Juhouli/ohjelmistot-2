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


a = 1
oliot = []
for i in range(0,10):
    oliot.append(Auto(f"ABC-{a}",randint(100,200,)))
    a = a + 1

while oliot[0].kuljettumatka < 10000 and oliot[1].kuljettumatka < 10000 and oliot[2].kuljettumatka < 10000 and oliot[3].kuljettumatka < 10000 and oliot[4].kuljettumatka < 10000 and oliot[5].kuljettumatka < 10000 and oliot[6].kuljettumatka < 10000 and oliot[7].kuljettumatka < 10000 and oliot[8].kuljettumatka < 10000 and oliot[9].kuljettumatka < 10000:
    for i in range(0,10):
        oliot[i].kiihdyta(randint(-10, 15))
        oliot[i].kulje(1)

print("Rekisteritunnus  Huippunopeus  Nopeus  Kuljettumatka")
for i in range(0,9):
    print(f"{oliot[i].rekisteritunnus}            {oliot[i].huippunopeus}           {oliot[i].nopeus}     {oliot[i].kuljettumatka}")

print(f"{oliot[9].rekisteritunnus}           {oliot[9].huippunopeus}           {oliot[9].nopeus}     {oliot[9].kuljettumatka}")



