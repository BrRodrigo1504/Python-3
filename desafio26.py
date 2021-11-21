n=str(input('Digite uma frase:')).strip().upper()
print('A letra A apareceu {} vezes nessa frase'.format(n.count('A')) )
print('A primeira letra A apareceu na posicao {}'.format(n.find('A')))
print('A última letra A apareceu na posição {}'.format(n.rfind('A')))