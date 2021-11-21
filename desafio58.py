from random import randint

cont = 1
pc = randint(1, 10)
print('-=-' * 20)
print('\033[4;34mVou pensar em um numero entre 0 e 10, tente adivinhar!!\033[m')
print('-=-' * 20)
jogador = int(input('Qual foi o número que eu pensei? '))

while jogador != pc:
    jogador = int(input('O número está incorreto, tente novamente!'))
    cont += 1

if cont > 3:
    print('\033[4;31mFinalmente!!Voce demorou {} tentativas até acertar!!\033[m'.format(cont))
elif cont < 3:
    print('\033[4;35mParabéns, voce conseguiu!! Foram {} tentativa(s) até acertar!!'.format(cont))