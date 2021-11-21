from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0 , 2)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual é a sua jogada?'))
print('O computador jogou {}'.format(itens[pc]))
print('Jogador jogou {}'.format(itens[jogador]))