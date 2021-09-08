from formulas import conta_palavras, txt_string

arq_texto = txt_string(str(input('Digite o nome do arquivo que você quer contar as palavras: ')))
palavra = input('Digite a palavra que você quer contar: ')

print(f'A palavra {palavra} aparece {conta_palavras(arq_texto.lower(), palavra.lower())} vezes no arquivo de texto mencionado.')
