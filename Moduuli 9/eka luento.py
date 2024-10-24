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

a = 0
oliot = []
for i in range(1,10):
    oliot.append(Auto(f"ABC-{a}",randint(100,200,)))
    a = a + 1

while oliot[0].kuljettumatka < 10000:
    oliot[0].kiihdyta(randint(-10, 15))
    oliot[0].kulje(1)

print("Rekisteritunnus  Huippunopeus  Nopeus  Kuljettumatka")
print(f"{oliot[1].rekisteritunnus}            {oliot[1].huippunopeus}           {oliot[1].nopeus}     {oliot[1].kuljettumatka}")

while oliot[0].kuljettumatka < 10000 and oliot[1].kuljettumatka < 10000 and oliot[2].kuljettumatka < 10000 and oliot[3].kuljettumatka < 10000 and oliot[4].kuljettumatka < 10000 and oliot[5].kuljettumatka < 10000 and oliot[6].kuljettumatka < 10000 and oliot[7].kuljettumatka < 10000 and oliot[8].kuljettumatka < 10000 and oliot[9].kuljettumatka < 10000:
    oliot[0].kiihdyta(randint(-10, 15))
    oliot[0].kulje(1)
    oliot[1].kiihdyta(randint(-10, 15))
    oliot[1].kulje(1)
    oliot[2].kiihdyta(randint(-10, 15))
    oliot[2].kulje(1)
    oliot[3].kiihdyta(randint(-10, 15))
    oliot[3].kulje(1)
    oliot[4].kiihdyta(randint(-10, 15))
    oliot[4].kulje(1)
    oliot[5].kiihdyta(randint(-10, 15))
    oliot[5].kulje(1)
    oliot[6].kiihdyta(randint(-10, 15))
    oliot[6].kulje(1)
    oliot[7].kiihdyta(randint(-10, 15))
    oliot[7].kulje(1)
    oliot[8].kiihdyta(randint(-10, 15))
    oliot[8].kulje(1)
    oliot[9].kiihdyta(randint(-10, 15))
    oliot[9].kulje(1)
print("Rekisteritunnus  Huippunopeus  Nopeus  Kuljettumatka")
print(f"{auto1.rekisteritunnus}            {auto1.huippunopeus}           {auto1.nopeus}     {auto1.kuljettumatka}")
print(f"{auto2.rekisteritunnus}            {auto2.huippunopeus}           {auto2.nopeus}     {auto2.kuljettumatka}")
print(f"{auto3.rekisteritunnus}            {auto3.huippunopeus}           {auto3.nopeus}     {auto3.kuljettumatka}")
print(f"{auto4.rekisteritunnus}            {auto4.huippunopeus}           {auto4.nopeus}     {auto4.kuljettumatka}")
print(f"{auto5.rekisteritunnus}            {auto5.huippunopeus}           {auto5.nopeus}     {auto5.kuljettumatka}")
print(f"{auto6.rekisteritunnus}            {auto6.huippunopeus}           {auto6.nopeus}     {auto6.kuljettumatka}")
print(f"{auto7.rekisteritunnus}            {auto7.huippunopeus}           {auto7.nopeus}     {auto7.kuljettumatka}")
print(f"{auto8.rekisteritunnus}            {auto8.huippunopeus}           {auto8.nopeus}     {auto8.kuljettumatka}")
print(f"{auto9.rekisteritunnus}            {auto9.huippunopeus}           {auto9.nopeus}     {auto9.kuljettumatka}")
print(f"{auto10.rekisteritunnus}           {auto10.huippunopeus}           {auto10.nopeus}     {auto10.kuljettumatka}")







auto1 = Auto("ABC-1", randint(100, 200))
auto2 = Auto("ABC-2", randint(100, 200))
auto3 = Auto("ABC-3", randint(100, 200))
auto4 = Auto("ABC-4", randint(100, 200))
auto5 = Auto("ABC-5", randint(100, 200))
auto6 = Auto("ABC-6", randint(100, 200))
auto7 = Auto("ABC-7", randint(100, 200))
auto8 = Auto("ABC-8", randint(100, 200))
auto9 = Auto("ABC-9", randint(100, 200))
auto10 = Auto("ABC-10", randint(100, 200))

while auto1.kuljettumatka < 10000 and auto2.kuljettumatka < 10000 and auto3.kuljettumatka < 10000 and auto4.kuljettumatka < 10000 and auto5.kuljettumatka < 10000 and auto6.kuljettumatka < 10000 and auto7.kuljettumatka < 10000 and auto8.kuljettumatka < 10000 and auto9.kuljettumatka < 10000 and auto10.kuljettumatka < 10000 and auto10.kuljettumatka < 10000:
    auto1.kiihdyta(randint(-10, 15))
    auto1.kulje(1)
    auto2.kiihdyta(randint(-10, 15))
    auto2.kulje(1)
    auto3.kiihdyta(randint(-10, 15))
    auto3.kulje(1)
    auto4.kiihdyta(randint(-10, 15))
    auto4.kulje(1)
    auto5.kiihdyta(randint(-10, 15))
    auto5.kulje(1)
    auto6.kiihdyta(randint(-10, 15))
    auto6.kulje(1)
    auto7.kiihdyta(randint(-10, 15))
    auto7.kulje(1)
    auto8.kiihdyta(randint(-10, 15))
    auto8.kulje(1)
    auto9.kiihdyta(randint(-10, 15))
    auto9.kulje(1)
    auto10.kiihdyta(randint(-10, 15))
    auto10.kulje(1)
print("Rekisteritunnus  Huippunopeus  Nopeus  Kuljettumatka")
print(f"{auto1.rekisteritunnus}            {auto1.huippunopeus}           {auto1.nopeus}     {auto1.kuljettumatka}")
print(f"{auto2.rekisteritunnus}            {auto2.huippunopeus}           {auto2.nopeus}     {auto2.kuljettumatka}")
print(f"{auto3.rekisteritunnus}            {auto3.huippunopeus}           {auto3.nopeus}     {auto3.kuljettumatka}")
print(f"{auto4.rekisteritunnus}            {auto4.huippunopeus}           {auto4.nopeus}     {auto4.kuljettumatka}")
print(f"{auto5.rekisteritunnus}            {auto5.huippunopeus}           {auto5.nopeus}     {auto5.kuljettumatka}")
print(f"{auto6.rekisteritunnus}            {auto6.huippunopeus}           {auto6.nopeus}     {auto6.kuljettumatka}")
print(f"{auto7.rekisteritunnus}            {auto7.huippunopeus}           {auto7.nopeus}     {auto7.kuljettumatka}")
print(f"{auto8.rekisteritunnus}            {auto8.huippunopeus}           {auto8.nopeus}     {auto8.kuljettumatka}")
print(f"{auto9.rekisteritunnus}            {auto9.huippunopeus}           {auto9.nopeus}     {auto9.kuljettumatka}")
print(f"{auto10.rekisteritunnus}           {auto10.huippunopeus}           {auto10.nopeus}     {auto10.kuljettumatka}")


