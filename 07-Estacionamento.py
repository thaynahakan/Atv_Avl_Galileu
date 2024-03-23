
'''   
Discente: Kalyne Rodrigues de Melo  Matrícula: 20232014050032
Discente: Thayna Bittencourt Baima Matrícula: 20241014050030

Questão 7 -Em um estacionamento, as tarifas são as seguintes (cumulativas):
Até duas horas: R$ 8,00/hora ou fração;
Entre três e quatro horas: R$ 5,00/hora ou fração;
Horas seguintes: R$ 3,00/hora ou fração.
Depois de 12h, o custo passa a ser fixo: R$ 30,00
Faça um programa que leia o número de minutos que um veículo permaneceu no estacionamento e exiba o valor a ser pago pelo responsável.

Como exemplo, considere que o carro ficou 310 minutos no estacionamento; deve pagar: R$ 16,00 (pelas duas primeiras horas) + R$ 10,00 (pela terceira e quarta horas) + R$ 6,00 (pela quinta hora e fração da sexta hora): total de R$ 32,00'''

# Lê o número de minutos que o veículo permaneceu estacionado

import math
minutos = int(input("Digite o número de minutos que o veículo permaneceu no estacionamento: "))

# Calcula o número de horas completas e a fração de hora restante
horas_completas = math.ceil(minutos / 60) #vem em forma de numeros inteiros.
fracao_hora = minutos % 60

# Calcula o valor a ser pago
if horas_completas <= 2:
    valor_total = horas_completas * 8 # 8 reais por hora / 2 horas 16 reais
elif horas_completas <= 4:
    valor_total = horas_completas* 8+ (horas_completas - 2) * 5 # a primeira parte é partindo do pressuposto de que ja tem 16 reais das primeiras 2 horas + (a variável das horas completas menos o valor dessas duas horas que já fizemos a conta) vezes 5, as horas seguintes terão um adcional de 5 reais a hora.
elif horas_completas <= 12:
    valor_total = 16 + 10 + (horas_completas - 4) * 3 #Horas seguintes: R$ 3,00/hora ou fração.

else:
    valor_total = 30

# Adiciona o valor proporcional pela fração de hora
if fracao_hora > 0:
    if horas_completas < 2:
        valor_total += 8
    elif horas_completas < 4:
        valor_total += 5
    else:
        valor_total += 3

if valor_total > 30:  #nessa parte perguntei a Você professor Galileu e após 12 horas o valor final é 30 reais e só.
    valor_total = 30

# Exibe o valor total a ser pago
print(f"Valor a ser pago: R$ {valor_total:.2f}")
