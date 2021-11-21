a = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para binário é igual a {}'.format(a, bin(a)))
elif opção == 2:
    print('{} convertido para Octal é igual a {}'.format(a, oct(a)))
elif opção == 3:
    print('{} convertido para Hexadecimal é igual a {}'.format(a, hex(a)))