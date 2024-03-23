'''   Discente: Kalyne Rodrigues de Melo  Matrícula: 20232014050032
      Discente: Thayna Bittencourt Baima Matrícula: 20241014050030
Faça um programa que leia os 3 lados de um triângulo e informe o seu tipo:

Triângulo equilátero: possui os três lados com medidas iguais.
Triângulo isósceles: possui dois lados com medidas iguais.
Triângulo escaleno: possui os três lados com medidas diferentes.

Lembrando que todos os lados devem ser positivos e que:,'''

print('Analisador de triângulos das Meninas de Redes do IF!')

l1 = float(input('Lado A: '))
l2 = float(input('Lado B: '))
l3 = float(input('Lado C: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Pode formar um triângulo:')
    if l1 == l2 == l3:
        print(' EQUILÁTERO')
    elif l1 != l2 != l3 != l1:
        print(' ESCALENO')
    else:
        print(' ISÓSCELES')
else:
    print('Os segmentos acima não podem formar um triângulo!')