from math import pi as pi

class Circulo:
    def __init__(self, raio):
        self.raio = raio
        self.area = pi * raio ** 2
        self.perimetro = 2 * pi * raio

    def imprimir(self):
        return print(f'Raio: {self.raio} - Área: {self.area} - Perímetro: {self.perimetro}')

if __name__ == '__main__':
    bolinha = Circulo(7)
    bolinha.imprimir()