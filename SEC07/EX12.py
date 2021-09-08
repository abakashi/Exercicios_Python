valores = []
for i in range(5):
    entrada = int(input(f'Insira o {i+1}º número: '))
    valores.append(entrada)
med = sum(valores) / len(valores)
maior = max(valores)
menor = min(valores)
print(f'{med:.2f} é a média entre os valores.\n'
      f'{maior} é o maior número digitado.\n'
      f'{menor} é o menor número digitado.')
