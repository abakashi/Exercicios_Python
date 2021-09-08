class Equipamento:
    def __init__(self, att01, att02):
        self.__att01 = att01
        self.__att02 = att02

    @property
    def att01(self):
        return self.__att01

    @att01.setter
    def att01_setter(self, valor):
        self.__att01 = valor

    @property
    def att02(self):
        return self.__att02

    @att02.setter
    def att02_setter(self, valor):
        self.__att02 = valor

    def exibe(self):
        return self.__dict__



class Computador(Equipamento):

    def __init__(self, att01, att02, att03, att04):
        super().__init__(att01=att01, att02=att02)
        self.__att03 = att03
        self.__att04 = att04

    @property
    def att03(self):
        return self.__att03

    @att03.setter
    def att03_setter(self, valor):
        self.__att03 = valor

    @property
    def att04(self):
        return self.__att04

    @att04.setter
    def att04_setter(self, valor):
        self.__att04 = valor

class TestaEquipamento(Equipamento):
    def __init__(self, att01, att02, att03, att04):
        super().__init__(att01=att01, att02=att02)
        self.__att03 = att03
        self.__att04 = att04

    def main(self):
        return self.__dict__


computador = Computador('batata', 'cuzinho', 'asses', 'butts')
print(computador.att03)
computador.att03_setter = 'marcelo'
print(computador.att03)
print(computador.__dict__)
print(computador.exibe())