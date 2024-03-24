'''
Discente: Kalyne Rodrigues de Melo  Matrícula: 20232014050032
Discente: Thayna Bittencourt Baima  Matrícula: 20241014050030
O número de dias decorridos entre duas datas é importante em uma infinidade de situações da vida cotidiana.
Faça um programa que recebe inicialmente dois valores (dia inicial e mês inicial), depois mais dois valores (dia final, mês final), ao final deve indicar quantos dias se passaram entre as datas (considere que o ano não é bissexto). 

Exemplos:
02 de 05 até 03 de 05 - 1 dia
27 de 04 até 03 de 05 - 6 dias
03 de 02 até 03 de 05 - 79 dias
Não esqueça de verificar se a data inicial é menor ou igual à data final. 

Dica: conte o número de dias até cada uma das datas e subtraia esses números.'''
from datetime import datetime

# Recebe as datas iniciais
dia_inicial = int(input("Digite o dia inicial: "))
mes_inicial = int(input("Digite o mês inicial: "))

# Recebe as datas finais
dia_final = int(input("Digite o dia final: "))
mes_final = int(input("Digite o mês final: "))

# Cria objetos datetime para as datas
# datetime recebe 3 valores : o ano , o mês e o dia
data_inicial = datetime(year=2023, month=mes_inicial, day=dia_inicial)
data_final = datetime(year=2023, month=mes_final, day=dia_final)

# Calcula a diferença em dias entre as datas
diferenca = (data_final - data_inicial).days

# Exibe o resultado
print(f"Número de dias decorridos entre as datas: {diferenca} dias.")