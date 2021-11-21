n1 = int(input('Difite um numero : '))
n2 = int(input('Digite outro numero: '))
s = n1 + n2
m = n1 * n2
opção = 0
while opção != 5:
    print(''' Selecione opção voce deseja:
[ 1 ] Soma
[ 2 ] Multiplicação
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa''')
    opção = int(input('Digite a opção desejada: '))
    if opção == 1:
        print('A soma entre os dois valores é {}'.format(s))
    elif opção == 2:
        print('A multiplicação dos dois valores é {}'.format(m))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('O maior número é {}'.format(maior))
    elif opção == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
    elif opção == 5:
        print('Finalizando.....')
    else:
        print('Opção invalida.Tente Novamente!!')