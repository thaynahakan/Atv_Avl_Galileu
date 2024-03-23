'''
Discente: Kalyne Rodrigues de Melo  Matrícula: 20232014050032
Discente: Thayna Bittencourt Baima  Matrícula: 20241014050030

Faça um programa que leia um valor inteiro correspondente a um ano e diga se o ano informado é bissexto ou não. Um ano é bissexto se é múltiplo de 400, ou se é múltiplo de 4, mas não de 100. '''

import calendar

ano = int(input("Digite um ano: "))

if calendar.isleap(ano):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")


'''Neste código, após importar a biblioteca calendar, você simplesmente chama a função isleap() com o ano fornecido como argumento. Se o ano for bissexto, a função retorna True e uma mensagem indicando que o ano é bissexto é exibida. Caso contrário, a função retorna False e uma mensagem indicando que o ano não é bissexto é exibida.'''

# Forma sem importar a biblioteca

ano = int(input('digite o ano: '))
   
if ano % 4 ==  0 and ano % 100 != 0:
    print('O ano é bissexto!')
else:
    if ano % 400 == 0 and ano % 100 != 0:
        print("O ano é bissexto!")
    else:
        print("ano NÃO é bissexto!")