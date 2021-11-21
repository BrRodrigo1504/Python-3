a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = a/b
if c<= 0.99:
    print('{} é menor que {}'.format(a, b))
elif c== 1:
    print('Os dois numeros são iguais')
elif c>=1.01:
    print('{} é maior que {}'.format(a, b))