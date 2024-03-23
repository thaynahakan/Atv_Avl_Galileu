'''   Discente: Kalyne Rodrigues de Melo  Matrícula: 20232014050032
      Discente: Thayna Bittencourt Baima Matrícula: 20241014050030'''

#Faça um programa que aceita um número de até 4 dígitos (0 a 9999) e exiba a soma dos seus algarismos.

''' Calcula a soma dos dígitos individualmente
digito_1 = numero // 1000: Esta operação extrai o dígito na posição de milhares. Quando dividimos o número inteiro por 1000, o resultado será o dígito na posição de milhares. Isso ocorre porque a divisão inteira remove todos os dígitos à direita do dígito de milhares, deixando apenas o dígito na posição de milhares.

digito_2 = (numero // 100) % 10: Esta operação extrai o dígito na posição de centenas. Primeiro, dividimos o número inteiro por 100, o que remove todos os dígitos à direita do dígito de centenas. Em seguida, usamos o operador % 10 para obter o resto da divisão por 10, o que nos dá o dígito na posição de centenas. Isso ocorre porque, depois de dividir por 100, o dígito de centenas se torna o dígito das dezenas, e usar o operador % 10 extrai esse dígito.

digito_3 = (numero // 10) % 10: Esta operação extrai o dígito na posição das dezenas. Primeiro, dividimos o número inteiro por 10, o que remove todos os dígitos à direita do dígito das dezenas. Em seguida, usamos o operador % 10 para obter o resto da divisão por 10, o que nos dá o dígito na posição das dezenas.

digito_4 = numero % 10: Esta operação extrai o dígito na posição das unidades. Usamos o operador % 10 para obter o resto da divisão por 10, o que nos dá o dígito na posição das unidades.'''

numero = int(input('Digite um número de até 4 dígitos de 0 a 9999: '))
if numero <= 0 or numero > 9999:
    print('O número deve ter estar entre 0 e 9999.')
    print(f'Você digitou {numero}')
else:
    if numero < 10:
        soma = numero
    elif numero < 100:
        digito1 = numero // 10
        digito2 = numero % 10
        soma = digito1 + digito2
    elif numero < 1000:
        digito1 = numero // 100
        digito2 = (numero // 10) % 10
        digito3 = numero % 10
        soma = digito1 + digito2 + digito3
    else:
        digito1 = numero // 1000
        digito2 = (numero // 100) % 10
        digito3 = (numero // 10) % 10
        digito4 = numero % 10
        soma = digito1 + digito2 + digito3 + digito4

    print(f'A soma dos dígitos do numero {numero} que você digitou, é: {soma}.')
#calcula a soma dos digitos:
