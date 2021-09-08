class Quadrado:
    def __init__(self, lado):
        self.lado = lado
        self.area = lado ** 2
        self.perimetro = lado + lado + lado + lado

    def imprimir(self):
        return print(f'Lado: {self.lado} - Área: {self.area} - Perímetro: {self.perimetro}')

if __name__ == '__main__':
    cadradu = Quadrado(25)
    cadradu.imprimir()