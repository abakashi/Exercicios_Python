degrau = float(input('Insira a altura do degrau em cm: '))
objetivo = float(input('Insira a altura desejada em metros: '))
deg_m = degrau / 100
n_deg = objetivo / deg_m
print(f'O número ne degraus será {int(n_deg)}.')
