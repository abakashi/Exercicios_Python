class Pessoa:
    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    def dados(self):
        return f'{str(self.__nome).title()} - Idade: {self.__idade} - Altura: {self.__altura}'

m_dict = [{'nome': 'Marco Cruz', 'idade': 32, 'altura': 1.76}, {'nome': 'Marcelo Cruz', 'idade': 24, 'altura': 1.76}]

for pessoa in m_dict:
    pessoa = Pessoa(pessoa['nome'], pessoa['idade'], pessoa['altura'])
    print(pessoa.dados())

