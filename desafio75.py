cont = 0

n = (int(input('Digite um número: ')),
    int(input('Digite um número: ')),
    int(input('Digite um número: ')),
    int(input('Digite um número: ')))
print(f'Voce digitou os valores {n}')
print(f'O numero 9 apareceu {n.count(9)} vezes' )
print(f'O número 3 apareceu na {n.index(3)+1}ª posição')
print('Os valores pares digitados foram ', end='')
for a in n:
    if a % 2 == 0:
        print(a, end= ' ')
