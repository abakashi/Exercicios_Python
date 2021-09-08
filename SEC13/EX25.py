"""
Agenda de telefones

Banco de dados: BD_EX25.bin

"""
from formulas import contact_store as armazenar, print_contacts as mostrar_contatos, contact_delete as apagar,\
    contact_show as mostrar, letter_contact as contatos_com_a_letra, month_birthdays as aniversariantes

from os import system as sistema

while True:
    sistema('cls')
    print('\nAgenda de telefones\nEscolha uma das opções abaixo:\n')
    opt = input('A - Inserir Contato;\n'
                'B - Remover contato;\n'
                'C - Pesquisar um contato pelo nome;\n'
                'D - Listar todos os contatos;\n'
                'E - Pesquisar contato por letra;\n'
                'F - Mostrar os aniversariantes do mês;\n'
                '* - Para sair digite "Sair".\n- ')
    if opt.lower() == 'a':
        nome = input('Insira o nome do contato: ')
        telefone = input('Insira o número de telefone do contato: ')
        data = []
        for i in range(3):
            dado = ''
            if i == 0:
                dado = 'dia (DD)'
            if i == 1:
                dado = 'mês (MM)'
            if i == 2:
                dado = 'ano (AAAA)'
            data.append(input(f'Insira o {dado} da data de nascimento do contato {nome.title()}: '))
        niver = f'{data[0]}/{data[1]}/{data[2]}'
        armazenar(nome.title(), telefone, niver)
        seguir = input('Armazenado!\nGostaria de continuar? (S/N)')
        if seguir.lower() == 's':
            continue
        if seguir.lower() == 'n':
            break
        else:
            break
    elif opt.lower() == 'b':
        nome = input('Insira o nome do contato que você quer apagar: ')
        apagar(nome.title())
        seguir = input('Gostaria de continuar? (S/N)')
        if seguir.lower() == 's':
            continue
        if seguir.lower() == 'n':
            break
        else:
            break
    elif opt.lower() == 'c':
        nome = input('Insira o nome do contato que você quer mostrar: ')
        mostrar(nome.title())
        seguir = input('Gostaria de continuar? (S/N)')
        if seguir.lower() == 's':
            continue
        if seguir.lower() == 'n':
            break
        else:
            break
    elif opt.lower() == 'd':
        mostrar_contatos()
        seguir = input('Gostaria de continuar? (S/N)')
        if seguir.lower() == 's':
            continue
        if seguir.lower() == 'n':
            break
        else:
            break
    elif opt.lower() == 'e':
        letra = input('Insira o caractere (apenas a letra ou número) para a qual deseja\nfazer a pesquisa: ')
        while len(letra) != 1:
            letra = input('Você deve digitar apenas um caractere!\nTente de novo: ')
        contatos_com_a_letra(letra)
        seguir = input('Gostaria de continuar? (S/N)')
        if seguir.lower() == 's':
            continue
        if seguir.lower() == 'n':
            break
        else:
            break
    elif opt.lower() == 'f':
        aniversariantes()
        seguir = input('Gostaria de continuar? (S/N)')
        if seguir.lower() == 's':
            continue
        if seguir.lower() == 'n':
            break
        else:
            break
    if opt.lower() == 'sair':
        break
    else:
        print('Opção inválida.')
        seguir = input('Gostaria de continuar? (S/N)')
        if seguir.lower() == 's':
            continue
        if seguir.lower() == 'n':
            break
        else:
            break
