"""
nome = 'Marco Antonio da Silva Cruz'
nome2 = ''
for letra in nome:
    if letra.isupper():
        nome2 += letra.lower()
    elif letra.islower():
        nome2 += letra.upper()
    else:
        nome2 += letra
print(nome2)
if type(nome) is str:
    print('mandou bem')
else:
    print('mandou mal')
------------------------------------------------
arq1 = 'teste1'
arq2 = 'teste2'
arq3 = 'teste3'

arq1_w = open(str(arq1) + '.txt', 'w')
arq2_w = open(str(arq2) + '.txt', 'w')

arq1_w.write(entrada1)
arq1_w.close()
arq2_w.write(entrada2)
arq2_w.close()

arq1_r = open(str(arq1) + '.txt', 'r')
arq2_r = open(str(arq2) + '.txt', 'r')
arq3_w = open(str(arq3) + '.txt', 'w')
arq3_w.write(arq1_r.read() + ' ' + arq2_r.read())
arq1_r.close()
arq2_r.close()
arq3_w.close()
------------------------------------------------
file = open('cities_br.txt', 'r')
lista = file.readlines()
file.close()
lista2 = [cidade.replace('\n', '') if '\n'in cidade else cidade for cidade in lista]
lista3 = [cidade.split(': ') for cidade in lista2]
cidades = {cidade[0]: int(cidade[1]) for cidade in lista3}
cidades_ordenadas = sorted(cidades.items(), reverse=True, key=lambda x: x[1])

with open('sorted_cities.txt', 'w') as sort_city:
    for cidade in cidades_ordenadas:
        sort_city.write(str(cidade[0])+': '+str(cidade[1]) + '\n')
------------------------------------------------
file = open('cidades_decrescente.txt', 'r')
leitura = file.read()
file.close()
leit_trat = leitura.replace('\n', ' ')
print(leit_trat)
------------------------------------------------
file = open('texto_sobre_marmotas.txt', 'r', encoding='utf-8')
linhas = file.readlines()
file.seek(0)
txt_string = file.read()
num_carac = len(txt_string)
file.close()
num_linhas = len(linhas)
palavras = txt_string.split(' ')
print(num_carac, num_linhas, len(palavras), sep=', ')
------------------------------------------------
nome = 'Marco'
telefone = '971225237'
with open('telefones.txt', 'a', encoding='utf-8') as entrada:
    entrada.write('Nome: ' + str(nome) + ' - Telefone: ' + str(telefone) + '\n')
------------------------------------------------
with open('date.txt', 'r', encoding='utf-8') as file:
    data = [int(data) for data in file.read().split()]

nome = input('Insira seu nome: ')
birth = input('Insira sua data de nascimento (DD MM AAAA): ')
birth_list = [int(data) for data in birth.split()]

with open(str(nome).capitalize().replace(' ', '_') + '.txt', 'w', encoding='utf-8') as file:
    if data[1] >= birth_list[1]:
        file.write(str(nome).capitalize() + ' - Idade: ' + str(data[2] - birth_list[2]) + ' anos.\n')
    else:
        file.write(str(nome).capitalize() + ' - Idade: ' + str(data[2] - birth_list[2] - 1) + ' anos.\n')
------------------------------------------------
def bin_to_str(binario):
    binario = str(binario)
    caractere = ''
    string = ''
    tamanho = len(binario)
    k = 1
    for j in binario:
        if j != ' ':
            caractere += j
            if k == tamanho:
                string += chr(int(caractere, 2))
        else:
            string += chr(int(caractere, 2))
            caractere = ''  # 0x101100110
        k += 1
    return string

def str_to_bin(string):
    binario = ''
    for i in string:
        binario += bin(ord(i))[2::] + ' '
    return binario


print(bin_to_str(str_to_bin('Marco antonio da silva cruz')))

------------------------------------------------
from formulas import print_contacts as contatos, contact_store as armazena_contato
# Nome - Telefone -- Aniversario
lista = ['Marco Cruz - 22324957', 'Marcelo Cruz - 971225237']

nome = 'Marco'
telefone = '21 971225237'
niver = '23/03/1988'

#armazena_contato('Antonio', '21 22410023', '18/01/1952')
contatos()

------------------------------------------------
with open('BD_EX25.bin', 'r') as banco_de_dados:
    contatos = {contato[0].lower(): contato[1] for contato in
                [contato.split(' - ') for contato in
                 sorted([bin_to_str(contato.replace('\n', '')) for contato in
                         banco_de_dados.readlines()])]}

try:
    contatos.pop(str(nome.lower()))
    with open('BD_EX25.bin', 'w') as banco_de_dados1:
        for contato in contatos.items():
            banco_de_dados1.write(str_to_bin(str(contato[0]).title() + ' - ' + str(contato[1])) + '\n')
    print(f'{nome.title()} foi apagado com sucesso.')

except:
    print(f'{nome.title()} Não foi encontrado.')
------------------------------------------------
with open('BD_EX25.bin', 'r') as banco_de_dados:
    contatos = {contato[0].lower(): contato[1] for contato in
                [contato.split(' - ') for contato in
                 sorted([bin_to_str(contato.replace('\n', '')) for contato in
                         banco_de_dados.readlines()])]}
try:
    return print(nome.title(), contatos[str(nome).lower()], sep=' - ')
except:
    return print(f'{nome.title()} não foi encontrado.')

letra = 'm'

with open('BD_EX25.bin', 'r') as banco_de_dados:
    ocorrencia = [contato for contato in [bin_to_str(contato.replace('\n', '')) for contato
                  in banco_de_dados.readlines()] if contato[0].lower() == letra.lower()]
    print(*ocorrencia, sep='\n')
------------------------------------------------
nome = 'mar'

with open('BD_EX25.bin', 'r') as banco_de_dados:
    contatos = {contato[0].lower(): contato[1] for contato in [contato.split(' - ') for contato in
                sorted([bin_to_str(contato.replace('\n', '')) for contato in banco_de_dados.readlines()])]}
    for name, info in contatos.items():
        if str(nome).lower() in name.lower():
            print(name.title(), info, sep=" - ")
------------------------------------------------
nome = 'Marco - 21 971225237 -- 23/03/1988'

print(nome.split(' -- ')[1][-10:-8])

print(str(datetime.date.today()).split('-')[1])
#-----------------------------------------------
with open('A:\\Documentos\\Python\\guppe\\venv\\SEC13\\BD_EX25.bin', 'r') as banco_de_dados:
    contatos = [contato.split(' -- ') for contato in [bin_to_str(contato.replace('\n', '')) for contato in
                banco_de_dados.readlines()]]
    niver = [f'{contato[0]} -- {contato[1]}' for contato in contatos if
             contato[1][3:5] == str(datetime.date.today()).split('-')[1]]
    print(niver)
------------------------------------------------
from formulas import bin_to_str, str_to_bin
import datetime
------------------------------------------------
def pares(max):
    contador = 0
    a = 0
    while contador < max:
        a += 2
        yield a
        contador += 1

numeros = set(pares(10))

print(numeros)
------------------------------------------------

"""

