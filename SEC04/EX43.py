valor = float(input('Insira o valor: '))
print(f'Com desconto a vista R$: {valor * 0.9:.2f}.\nParcela de R$: {valor / 3:.2f} em 3x sem juros.\nComissão de R$: {(valor * 0.9) * 0.05:.2f} no valor a vista.\nComissão de R$: {valor * 0.05:.2f} na venda parcelada.')
