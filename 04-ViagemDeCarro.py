'''   Discente: Kalyne Rodrigues de Melo  Matrícula: 20232014050032
      Discente: Thayna Bittencourt Baima Matrícula: 20241014050030
    
    Uma família fez uma viagem de carro e quer detalhes sobre o desempenho do veículo. Faça um programa que pergunta: 

o momento inicial da partida (hora e minuto), o momento de chegada (hora e minuto), o número de segundos parados para descanso, o número de litros de combustível gasto (em l), o preço do litro de combustível (em R$) e a distância percorrida (em Km); 

Após receber os dados, o programa informa dados típicos de um computador de bordo: 

o tempo de viagem (em segundos)
a velocidade média (Km/h) global e a velocidade média em movimento (Km/h)
o custo da viagem com combustível (em R$)
o desempenho do carro (em Km/l, l/h e R$/Km).'''

# Momento inicial da partida
hora_partida = int(input("Digite a hora de partida: "))
minuto_partida = int(input("Digite os minutos de partida: "))

# Momento de chegada
hora_chegada = int(input("Digite a hora de chegada: "))
minuto_chegada = int(input("Digite os minutos de chegada: "))

# Número de segundos parados para descanso
segundos_parados = int(input("Digite o número de segundos parados para descanso: "))

# Número de litros de combustível gasto
litros_combustivel = float(input("Digite o número de litros de combustível gasto (em litros): "))

# Preço do litro de combustível
preco_combustivel = float(input("Digite o preço do litro de combustível (em R$): "))

# Distância percorrida
distancia_percorrida = float(input("Digite a distância percorrida (em km): "))

# Cálculo do tempo de viagem em segundos
tempo_partida_segundos = hora_partida * 3600 + minuto_partida * 60
tempo_chegada_segundos = hora_chegada * 3600 + minuto_chegada * 60
tempo_total_segundos = tempo_chegada_segundos - tempo_partida_segundos - segundos_parados

# Cálculo da velocidade média global (Km/h)
velocidade_media_global = distancia_percorrida / (tempo_total_segundos / 3600)

# Cálculo da velocidade média em movimento (Km/h)
tempo_em_movimento_segundos = tempo_total_segundos - segundos_parados
velocidade_media_movimento = distancia_percorrida / (tempo_em_movimento_segundos / 3600)

# Cálculo do custo da viagem com combustível (em R$)
custo_combustivel = litros_combustivel * preco_combustivel

# Cálculo do desempenho do carro
desempenho_km_litro = distancia_percorrida / litros_combustivel
desempenho_litro_hora = litros_combustivel / (tempo_total_segundos / 3600)
desempenho_reais_km = custo_combustivel / distancia_percorrida

# Exibição dos resultados
print("\nDados típicos de um computador de bordo:")
print(f"Tempo de viagem: {tempo_total_segundos} segundos")
print(f"Velocidade média global: {velocidade_media_global:.2f} Km/h")
print(f"Velocidade média em movimento: {velocidade_media_movimento:.2f} Km/h")
print(f"Custo da viagem com combustível: R$ {custo_combustivel:.2f}")
print(f"Desempenho do carro:")
print(f"  - Km/l: {desempenho_km_litro:.2f} Km/l")
print(f"  - Litros/hora: {desempenho_litro_hora:.2f} l/h")
print(f"  - R$/Km: {desempenho_reais_km:.2f} R$/Km")
