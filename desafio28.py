from random import randint
computador = randint(0, 5) #faz o pc pensar
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador=int(input('Em que numero eu pensei?'))
if jogador == computador:
    print('Parabens!! Voce conseguiu me vencer!!')
else:
    print('GANHEI!! Eu pensei no numero {} e nao no {}!!'.format(computador, jogador))


