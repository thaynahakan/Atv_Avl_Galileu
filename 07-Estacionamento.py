'''
Discente: Kalyne Rodrigues de Melo  Matrícula: 20232014050032
Discente: Thayna Bittencourt Baima  Matrícula: 20241014050030
Questão 7 -Em um estacionamento, as tarifas são as seguintes (cumulativas):
Até duas horas: R$ 8,00/hora ou fração;
Entre três e quatro horas: R$ 5,00/hora ou fração;
Horas seguintes: R$ 3,00/hora ou fração.
Depois de 12h, o custo passa a ser fixo: R$ 30,00
Faça um programa que leia o número de minutos que um veículo permaneceu no estacionamento e exiba o valor a ser pago pelo responsável.

Como exemplo, considere que o carro ficou 310 minutos no estacionamento; deve pagar: R$ 16,00 (pelas duas primeiras horas) + R$ 10,00 (pela terceira e quarta horas) + R$ 6,00 (pela quinta hora e fração da sexta hora): total de R$ 32,00'''

# Lê o número de minutos que o veículo permaneceu estacionado# Lê o número de minutos que o veículo permaneceu estacionado
minutos = int(input("Digite o número de minutos que o veículo permaneceu no estacionamento: "))

# Calcula o número de horas completas e a fração de hora restante
horasTransformadas = minutos // 60
fracao_hora = minutos % 60
hora = horasTransformadas
minutos = fracao_hora
# Calcula o valor total com base nas horas completas
if horasTransformadas <= 2:
    valor_total = horasTransformadas * 8
elif horasTransformadas <= 4:
    valor_total = 16 + (horasTransformadas - 2) * 5
else:
    valor_total = 26 + (horasTransformadas - 4) * 3

# Adiciona o valor proporcional pela fração de hora
if fracao_hora > 0:
    if horasTransformadas < 2:
        valor_total += 8
    elif horasTransformadas < 4:
        valor_total += 5
    else:
        valor_total += 3

# Se a permanência for superior a 12 horas, adiciona o valor fixo de R$ 30,00
if horasTransformadas > 12:
    valor_total = 30

# Exibe o valor total a ser pago
print(f"Valor a ser pago por {hora}:{minutos} R$ {valor_total:.2f}")