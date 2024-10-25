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

    def siirry_kerrokseen(self, liiku):
        if liiku == self.sijainti:
            print(f"Kerros {self.sijainti}")
            return
        elif liiku < self.sijainti:
            liiku = self.sijainti - liiku
            for i in range(liiku):
                hissi.kerros_alas()
        elif liiku > self.sijainti:
            liiku = liiku - self.sijainti
            for i in range(liiku):
                hissi.kerros_ylos()


hissi = Hissi(2,9)
hissi.siirry_kerrokseen(8)
hissi.siirry_kerrokseen(2)