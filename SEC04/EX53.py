comp = float(input('Insira comprimento (metros): '))
larg = float(input('Insira a largura (metros): '))
p_cerca = float(input('Insira o valor do metro de cerca (Reais): '))
perimetro = comp + comp + larg + larg
tot_cerca = p_cerca * perimetro
print(f'O total gasto para cercar o terreno é de: R$:{tot_cerca:.2f}.')
