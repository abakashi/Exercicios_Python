while True:
    print(f'\nConversor de medidas de velocidade:\n'
          f'Selecione a opção desejada:\n'
          f'1 - Km/h para m/s\n'
          f'2 - m/s para Km/h\n'
          f'3 - Finalizar')
    op = int(input('Escolha a sua opção: '))
    if op > 3 or op <= 0:
            print('Opção inválida.')
    elif op == 3:
        print('\nPrograma finalizado.\n')
        break
    elif op == 2:
        vel = float(input('Insira a velocidade em m/s: '))
        v_k = vel * 3.6
        print(f'\n{vel} m/s é equivalente a {v_k:.2f} Km/h.\n')
    elif op == 1:
        vel = float(input('Insira a velocidade em Km/h: '))
        v_m = vel / 3.6
        print(f'\n{vel} Km/h é equivalente a {v_m:.2f} m/s.\n')
