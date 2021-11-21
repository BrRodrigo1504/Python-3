
tabela = ('Atlético-MG', 'Vasco', 'Intenacional', 'Bahia',
          'Athletico-PR', 'Grêmio', 'Atlético-GO', 'Santos',
          'Fluminense', 'Sport', 'São Paulo', 'Flamengo',
          'Palmeiras', 'Botafogo', 'Bragantino', 'Corinthians',
          'Goiás', 'Ceará', 'Fortaleza', 'Coritiba')

print('''Caso queira ver os:
Os 5 Primeiros colocados [1]
Os 4 ultimos colocados [2]
Os times em ordem alfabética [3]
Em que posicao está o Vasco [4]''')

numero = int(input('Digite qual opção acima voce deseja: '))

if numero == 1:
    print(tabela[:5])
elif numero == 2:
    print(tabela[-4:])
elif numero == 3:
    print(enumerate(tabela))
elif numero == 4:
    print(tabela.index('Vasco')+1)