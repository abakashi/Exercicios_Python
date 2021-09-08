class Retangulo:
    def __init__(self, largura, comprimento):
        self.largura = largura
        self.comprimento = comprimento
        self.area = largura * comprimento
        self.perimetro = (largura * 2) + (comprimento * 2)

    def imprimir(self):
        return print(f'Lado: {self.largura} x {self.comprimento} - Área: {self.area} - Perímetro: {self.perimetro}')

if __name__ == '__main__':
    cadradu = Retangulo(25, 30)
    cadradu.imprimir()