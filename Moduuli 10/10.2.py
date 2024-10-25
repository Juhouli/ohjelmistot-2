class Hissi:
    def __init__(self, alinkerros, ylinkerros):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.sijainti = self.alinkerros

    def kerros_alas(self):
        self.sijainti -= 1
        if self.sijainti < self.alinkerros:
            self.sijainti = self.alinkerros
        else:
            print(f"Kerros {self.sijainti}")

    def kerros_ylos(self):
        self.sijainti += 1
        if self.sijainti > self.ylinkerros:
            self.sijainti = self.ylinkerros
        else:
            print(f"Kerros {self.sijainti}")

    def siirry_kerrokseen(self, liiku, liikutettava):
        self.liikutettava = liikutettava
        if liiku == self.sijainti:
            print(f"Kerros {self.sijainti}")
            return
        elif liiku < self.sijainti:
            liiku = self.sijainti - liiku
            for i in range(liiku):
                liikutettava.kerros_alas()
        elif liiku > self.sijainti:
            liiku = liiku - self.sijainti
            for i in range(liiku):
                liikutettava.kerros_ylos()

class Talo:
    def __init__(self,alinkerros, ylinkerros, hissienmaara):
        self.alinkerros = alinkerros
        self.ylinkerros = ylinkerros
        self.hissienmaara = hissienmaara
        self.hissit = []
        for i in range(hissienmaara):
            self.hissit.append(Hissi(alinkerros, ylinkerros))

    def aja_hissia(self, hissinnumero, kohde):
        self.kohde = kohde
        self.hissinnumero = hissinnumero
        self.liikkuva_hissi = self.hissit[hissinnumero-1]

        paivitys = self.liikkuva_hissi.siirry_kerrokseen(kohde, self.liikkuva_hissi)
        self.liikkuva_hissi = paivitys



talo = Talo(2,9, 9)
talo.aja_hissia(2, 9)

