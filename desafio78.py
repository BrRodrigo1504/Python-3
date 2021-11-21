valores = []
maior = 0
menor = 0
for numeros in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {numeros}:')))
    if numeros == 0:
        maior = menor = valores[numeros]
    else:
        if valores[numeros] > maior:
            maior = valores[numeros]
        if valores[numeros] < menor:
            menor = valores[numeros]
print('=-'*30)
print(f'A sua lista de números é: {valores}')
print(f'O menor valor é o {menor} na posicao: ')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...')
print('=-'*30)
print(f'O maior valor é o {maior} na posição: ')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...')