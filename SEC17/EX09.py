class Moto:
    menormarcha = 0

    maiormarcha = 5

    def __init__(self, marca, modelo, cor, marcha):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.marcha = marcha
        self.ligada = False

    def imprimir(self):
        return print((self.marca, self.modelo, self.cor, self.marcha, self.ligada))

    def marcha_acima(self):
        if self.marcha < maiormarcha:
            self.marcha += 1
    def marcha_abaixo(self):
        if self.marcha > menormarcha:
            self.marcha -= 1

    def ligar(self):
        self.ligada = True

    def desligar(self):
        self.ligada = False
