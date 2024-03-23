''' Discente: Kalyne Rodrigues de Melo  Matrícula: 20232014050032
    Discente: Thayna Bittencourt Baima  Matrícula: 20241014050030
Faça um programa que solicite ao usuário um valor decimal positivo (esse valor corresponde ao valor de um saque em um terminal de caixa eletrônico) e que calcule a quantidade de cédulas de R$ 100,00, R$ 50,00, R$ 20,00, R$ 10,00, R$ 5,00 e R$ 2,00 e de moedas de R$ 1,00, R$ 0,50, R$ 0,25, R$ 0,10, R$ 0,05 e R$ 0,01.

Mostre apenas as cédulas/moedas que realmente necessitam ser dadas como troco.'''

print('ʕ•́ᴥ•̀ʔっ OI PESSOA ʕ•́ᴥ•̀ʔっ')
print('Bem vinda ao Sistema de Contagem de Trocos (✿◠‿◠) ')
print('(✿◠‿◠) ')

conta = float(input('Digite o valor da conta: '))
pagamento = float(input('Digite o valor do pagamento: '))

troco = pagamento - conta

print(f'O valor do troco é:  {troco:.2f}')

# Cálculo das cédulas de R$100
notasde100 = troco // 100
if notasde100 != 0:
    print('Notas de R$100:', int(notasde100))
    troco %= 100
# Cálculo das cédulas de R$50
notasde50 = troco // 50
if notasde50 != 0:
    print('Notas de R$50:', int(notasde50))
    troco %= 50

# Cálculo das cédulas de R$20
notasde20 = troco // 20
if notasde20 != 0:
    print('Notas de R$20:', int(notasde20))
    troco %= 20

# Cálculo das cédulas de R$10
notasde10 = troco // 10
if notasde10 != 0:
    print('Notas de R$10:', int(notasde10))
    troco %= 10

# Cálculo das cédulas de R$5
notasde5 = troco // 5
if notasde5 != 0:
    print('Notas de R$5:', int(notasde5))
    troco %= 5

# Cálculo das cédulas de R$2
notasde2 = troco // 2
if notasde2 != 0:
    print('Notas de R$2:', int(notasde2))
    troco %= 2

# Cálculo das moedas de R$1
moedasde1 = troco // 1
if moedasde1 != 0:
    print('Moedas de R$1:', int(moedasde1))
    troco %= 1

# Cálculo das moedas de R$0.50
moedasde050 = troco // 0.50
if moedasde050 != 0:
    print('Moedas de R$0.50:', int(moedasde050))
    troco %= 0.50

# Cálculo das moedas de R$0.25
moedasde025 = troco // 0.25
if moedasde025 != 0:
    print('Moedas de R$0.25:', int(moedasde025))
    troco %= 0.25

# Cálculo das moedas de R$0.10
moedasde010 = troco // 0.10
if moedasde010 != 0:
    print('Moedas de R$0.10:', int(moedasde010))
    troco %= 0.10

# Cálculo das moedas de R$0.05
moedasde005 = troco // 0.05
if moedasde005 != 0:
    print('Moedas de R$0.05:', int(moedasde005))
    troco %= 0.05

# Cálculo das moedas de R$0.01
moedasde001 = troco // 0.01
if moedasde001 != 0:
    print('Moedas de R$0.01:', int(moedasde001))
    troco %= 0.01

print(f'Obrigada por nos contratar ≧◠ᴥ◠≦')
print('Boa vida (✿◠‿◠) ')
