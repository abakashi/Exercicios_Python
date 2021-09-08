"""
Módulo de fórmulas e funções Python para os exercícios da seção 13.
"""
import datetime #import que eu tive que fazer.. T.T preguiça monstra.


def trocaletra(nome):
    """
    Troca as letras maiúsculas para minúsculas de uma string, seja qual for.
    :param nome: Parâmetro de entrada, deve ser necessáriamente uma string.
    :return: Retorna a mesma string trocando as letras maúsculas por minúsculas e vice versa.
    """
    nome2 = ''
    if type(nome) is not str:
        print('A entrada deve ser uma string.')
    else:
        for letra in nome:
            if letra.isupper():
                nome2 += letra.lower()
            elif letra.islower():
                nome2 += letra.upper()
            else:
                nome2 += letra
    return str(nome2)

# --------------------------------------------------------------
def junta_texto_arquivo(arq1, arq2, arq3, entrada1, entrada2):
    """
    Cria dois arquivos de texto (.txt) e junta os textos dos dois num terceiro.
    :param arq1: nome para o primeiro arquivo.
    :param arq2: nome para o segundo arquivo.
    :param arq3: nome para o arquivo da soma do texto dos dois primeiros.
    :param entrada1: entrada de texto para ser escrita no primeiro arquivo.
    :param entrada2: entrada de texto para ser escrita do segundo arquivo.
    :return: a função não possui retorno.
    """
    if type(arq1) is not str:
        print('Todos os parâmetros devem ser do tipo string.')
    elif type(arq2) is not str:
        print('Todos os parâmetros devem ser do tipo string.')
    elif type(arq3) is not str:
        print('Todos os parâmetros devem ser do tipo string.')
    elif type(entrada1) is not str:
        print('Todos os parâmetros devem ser do tipo string.')
    elif type(entrada2) is not str:
        print('Todos os parâmetros devem ser do tipo string.')
    else:
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

# --------------------------------------------------------------
def organ_cidade(arquivo_leitura, arquivo_saida):
    """
    Recebe um arquivo de texto (.txt) contendo uma lista de cidades e população e cria um novo arquivo da
    mesma extensão com os dados devidamente organizado pelo número decrescente de habitantes.
    :param arquivo_leitura: Arquivo de entrada da função
    :param arquivo_saida: Nome para o arquivo de saída.
    :return: A função não tem retorno.
    """
    try:
        with open(str(arquivo_leitura) + '.txt', 'r', encoding='utf-8') as file:
            cidades = {cidade[0]: int(cidade[1]) for cidade in [cidade.split(': ') for cidade in
                      [cidade.replace('\n', '') if '\n' in cidade else cidade for cidade in file.readlines()]]}

        cidades_ordenadas = sorted(cidades.items(), reverse=True, key=lambda x: x[1])

        with open(str(arquivo_saida) + '.txt', 'w', encoding='utf-8') as sort_city:
            for cidade in cidades_ordenadas:
                sort_city.write(str(cidade[0]) + ': ' + str(cidade[1]) + '\n')
    except:
        'As entradas devem ser obrigatóriamente caracteres alfabéticos.'

# --------------------------------------------------------------
def conta_palavras(texto, palavra):
    """
    Conta o número de ocorrências de uma palavra numa string.
    :param texto: Texto a ser analizado
    :param palavra: Palavra que será contada.
    :return: Número de ocorrência da palavra no texto.
    """
    if type(texto) is not str:
        print('O parâmetro de entrada DEVE ser uma string.')
    elif type(palavra) is not str:
        print('A palavra que deve ser buscada DEVE estar em formato string.')
    else:
        text = str(texto)
        word = str(palavra)
        return text.count(word)

# --------------------------------------------------------------
def txt_string(arquivo):
    """
    Transforma o conteúdo de qualquer arquivo .txt em uma string sem separadores de linha.
    :param arquivo: Nome do arquivo sem a extensão.
    :return: String do conteúdo do txt sem as quebras de linha.
    """
    if type(arquivo) is not str:
        print('O parâmetro deve ser uma string contendo o nome do arquivo sem extensão.')
    else:
        file = open(str(arquivo) + '.txt', 'r', encoding='utf-8')
        leitura = file.read()
        file.close()
        leit_trat = leitura.replace('\n', ' ')
        return  leit_trat

# --------------------------------------------------------------
def contador_palavras_linhas_caracs(arquivo):
    """
    Conta o número de linhas, caracteres e palavras contidas num arquivo de texto puro.
    :param arquivo: Nome do arquivo contendo o texto sem a sua extensão.
    :return: Informações no formato String
    """
    try:
        file = open(str(arquivo) + '.txt', 'r', encoding='utf-8')
        linhas = file.readlines()
        file.seek(0)
        txt_string = file.read()
        file.close()
        palavras = txt_string.split(' ')
        return f'O texto contém:\n{len(linhas)} linhas;\n{len(txt_string)} letras;\ne {len(palavras)} palavras.'
    except:
        return 'Algo deu errado, verifique se o nome do arquivo foi passado como uma string\nou se o arquivo de fato' \
               ' existe.'

# --------------------------------------------------------------
def anota_telefone(nome, telefone):
    """
    Insere as entradas de nome e telefone no arquivo telefones.txt
    :param nome: Nome da pessoa
    :param telefone: Telefone da pessoa
    :return: Não possui retorno.
    """
    with open('telefones.txt', 'a', encoding='utf-8') as entrada:
        entrada.write('Nome: ' + str(nome) + ' - Telefone: ' + str(telefone) + '\n')

# --------------------------------------------------------------
def calcula_idade(nome, idade):
    """
    Usa a data contida no arquivo 'date.txt' para calcular a idade de uma pessoa e armazená-la
    com o seu nome num arquivo de texto puro com seu nome.
    :param nome: Nome da pessoa em string
    :param idade: Lista contendo [DIA, MES, ANO(4 dígitos)]
    :return:
    """
    if type(nome) is not str:
        return print('O nome deve ser uma String')
    elif type(idade) is not list:
        return print('A idade deve ser sempre uma lista,\nPOS-0 = DIA\nPOS-1 = MES\nPOS-2 = ANO')
    else:
        try:
            with open('date.txt', 'r', encoding='utf-8') as file:
                data = [int(data) for data in file.read().split()]
            with open(str(nome).lower().replace(' ', '_') + '.txt', 'w', encoding='utf-8') as file:
                if data[1] >= idade[1]:
                    file.write(str(nome).title() + ' - Idade: ' + str(data[2] - idade[2]) + ' anos.\n')
                else:
                    file.write(str(nome).title() + ' - Idade: ' + str(data[2] - idade[2] - 1) + ' anos.\n')
            return print('Operação efetuada com sucesso!')
        except:
            return print('Algo deu errado!')

# --------------------------------------------------------------
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

# --------------------------------------------------------------
def str_to_bin(string):
    binario = ''
    for i in string:
        binario += bin(ord(i))[2::] + ' '
    return binario

#---------------------------------------------------------------
def contact_store(nome, telefone, niver):
    """
    Armazena um contato no banco de dados binário BD_EX25.bin
    :param nome: Nome do contato
    :param telefone: Número do telefone do contato
    :param niver: Data de aniversário do contato.
    :return: A função não tem retorno.    """
    with open('A:\\Documentos\\Python\\guppe\\venv\\SEC13\\BD_EX25.bin', 'a') as banco_de_dados:
        banco_de_dados.write(str_to_bin(str(nome) + ' - ' + str(telefone) + ' -- ' + str(niver)) + '\n')

# --------------------------------------------------------------
def print_contacts():
    """
    Retorna todos os contatos contidos no banco de dados.
    :return: Imprime todos os contatos contidos no banco de dados.
    """
    try:
        with open('A:\\Documentos\\Python\\guppe\\venv\\SEC13\\BD_EX25.bin', 'r') as banco_de_dados:
            contatos = sorted((bin_to_str(contato.replace('\n', '')) for contato in banco_de_dados.readlines()))
        return print(*contatos, sep='\n')
    except:
        print('Arquivo de banco de dados não encontrado.')

# --------------------------------------------------------------
def contact_delete(nome):
    """
    Apaga uma ocorrência na base de dados da agenda de contatos.
    :param nome: nome do contato a ser apagado.
    :return: retorna uma mensagem de sucesso ou de contato não encontrado.
    """
    with open('A:\\Documentos\\Python\\guppe\\venv\\SEC13\\BD_EX25.bin', 'r') as banco_de_dados:
        contatos = {contato[0].lower(): contato[1] for contato in [contato.split(' - ') for contato in
                    sorted([bin_to_str(contato.replace('\n', '')) for contato in banco_de_dados.readlines()])]}
    try:
        contatos.pop(str(nome.lower()))
        with open('A:\\Documentos\\Python\\guppe\\venv\\SEC13\\BD_EX25.bin', 'w') as banco_de_dados1:
            for contato in contatos.items():
                banco_de_dados1.write(str_to_bin(str(contato[0]).title() + ' - ' + str(contato[1])) + '\n')
        return print(f'{nome.title()} foi apagado com sucesso.')

    except:
        return print(f'{nome.title()} não foi encontrado.')

# --------------------------------------------------------------
def contact_show(nome):
    """
    Busca um contato pelo nome e o mostra na tela.
    :param nome: Nome do contato a ser procurado.
    :return: Exibe as informações do contato ou uma mensagem de contato não encontrado.
    """
    with open('A:\\Documentos\\Python\\guppe\\venv\\SEC13\\BD_EX25.bin', 'r') as banco_de_dados:
        contatos = {contato[0].lower(): contato[1] for contato in [contato.split(' - ') for contato in
                    sorted([bin_to_str(contato.replace('\n', '')) for contato in banco_de_dados.readlines()])]}
        ocorr = []
    try:
        for name, info in contatos.items():
            if str(nome).lower() in name.lower():
                ocorr.append(f'{name.title()} - {info}')
        return print(*ocorr, sep='\n')
    except:
        return print(f'{nome.title()} não foi encontrado.')

# --------------------------------------------------------------
def letter_contact(letra):
    """
    Retorna uma lista de pessoas contidas na lista de contato cujos nomes começam
    com a letra designada.
    :param letra: letra a ser usada de parâmetro.
    :return: Lista impressa ou mensagem de erro.
    """
    if len(letra) > 1:
        return print('Deve ser inserida apenas uma letra, maiúscula ou minúscula.')
    else:
        with open('A:\\Documentos\\Python\\guppe\\venv\\SEC13\\BD_EX25.bin', 'r') as banco_de_dados:
            ocorrencia = sorted((contato for contato in (bin_to_str(contato.replace('\n', '')) for contato
                          in banco_de_dados.readlines()) if contato[0].lower() == str(letra).lower()))
        if len(ocorrencia) == 0:
            return print('Nenhum contato com esta letra cadastrado.')
        else:
            return print(*ocorrencia, sep='\n')

# --------------------------------------------------------------
def month_birthdays():
    """
    Função que imprime os aniversariantes do mês corrente.
    :return: Lista com os aniversáriantes do mês corrente ou mensagem de que não
             há aniversariantes caso não hajam ocorrências.
    """
    with open('A:\\Documentos\\Python\\guppe\\venv\\SEC13\\BD_EX25.bin', 'r') as banco_de_dados:
        contatos = (contato.split(' -- ') for contato in (bin_to_str(contato.replace('\n', '')) for contato in
                    banco_de_dados.readlines()))
        niver = sorted((f'{contato[0]} -- {contato[1]}' for contato in contatos if
                 contato[1][3:5] == str(datetime.date.today()).split('-')[1]), key=lambda x: x[-10:-8])
    if len(niver) > 0:
        return print(*niver, sep='\n')
    else:
        return print('Não há aniversariantes neste mês.')

# --------------------------------------------------------------
