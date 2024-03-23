moedas = [100, 50, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]

conta = float(input('Valor da conta:'))
pago = float(input('Quanto você vai pagar?'))

troco = (pago - conta)

print(f'O valor do troco é {troco}.')

while troco > 0:

    n100 = troco // 100 #divisão inteira.
    troco = troco - n100 * 100 #troco % 200 resto da divisão por 200
    print(f'Notas de 100: {n100}')
    n50 = troco // 50
    troco = troco - n50 * 50
    print(f'Notas de 50: {n50}')
    n20 = troco // 20
    troco = troco - n20 * 20
    print(f'Notas de 20: {n20}')
    n10 = troco // 10
    troco = troco - n10 * 10
    print(f'Nota de 10: {n10}')
    n5 = troco // 5
    troco = troco - n5 * 5
    print(f'Notas de 5: {n5}')
    n2 = troco // 2
    troco = troco - n2 * 2
    print(f'Notas de 2: {n2}')
    n1 = troco // 1
    troco = troco - n1 * 1
    print(f'Notas de 1: {n1}')
    n050 = troco // 0.50
    troco = troco - n050 * 0.50
    print(f'Moedas de 0.50: {n050}')
    n025 = troco // 0.25
    troco = troco - n025 * 0.25
    print(f'Moedas de 0.25: {n025}')
    n010 = troco // 0.10
    troco = troco - n010 * 0.10
    print(f'Moedas de 0.10: {n010}')
    n005 = troco // 0.05
    troco = troco - n005 * 0.05
    print(f'Moedas de 0.05: {n005}')
    n001 = troco // 0.01
    troco = troco - n001 * 0.01
    print(f'Moedas de 0.01: {n001}')