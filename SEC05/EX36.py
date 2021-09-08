valor_venda = float(input('Insira o valor total da venda: '))
comiss = 0
if valor_venda >= 100_000:
    comiss = 700 + (valor_venda * 0.16)
elif valor_venda < 100_000 and valor_venda >= 80_000:
    comiss = 650 + (valor_venda * 0.14)
elif valor_venda < 80_000 and valor_venda >= 60_000:
    comiss = 600 + (valor_venda * 0.14)
elif valor_venda < 60_000 and valor_venda >= 40_000:
    comiss = 550 + (valor_venda * 0.14)
elif valor_venda < 40_000 and valor_venda >= 20_000:
    comiss = 500 + (valor_venda * 0.14)
elif valor_venda < 20_000:
    comiss = 400 + (valor_venda * 0.14)

print(f'O valor da comissão é de R$: {comiss:.2f}.')
