from datetime import date
def voto(ano):
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f' Com {idade} não pode votar.'
    elif 16 >= idade < 18 or idade > 65:
        return f' Com {idade} é opcional votar.'
    else:
        return f' Com {idade} é obrigatório votar.'


nasc = int(input('Qual seu ano de nascimento?'))
print(voto(nasc))