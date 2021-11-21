from random import randint
print('~' *30)
print('Jogo do Par ou Impar ')
print('~' *30)
v = 0
cont = 0
while True:
    jogador = int(input('Digite o seu número: '))
    computador = randint(0 , 10)
    total = jogador + computador
    tipo = ''
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar ?')).strip().upper()[0]
    tipo = str(input('Par ou Ímpar ?')).strip().upper()[0]
    print(f'Você jogou {jogador} e pc jogou {computador}. Total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce ganhou!!')
            v += 1
        else:
            print('Voce perdeu!')
            break

    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce ganhou!!')
            v += 1
    else:
        print('Voce perdeu!!')
        break

print(f'Voce ganhou {v} vezes até perder!')







