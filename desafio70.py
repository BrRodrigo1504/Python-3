total = cont = maior = menor = 0
barato = ' '
print('-------\033[31mLista de Compras\033[m------')
while True:
    produto = str(input('Digite o nome do produto: '))
    preço = float(input('Digite o valor do produto: '))
    total += preço

    if preço >= 1000:
        cont += 1
    if cont == 1:
        menor = maior = preço
        barato = produto
    else:
        if preço > maior:
            maior = preço
            barato = produto
        if preço < menor:
            menor = preço
            barato = produto

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
            break
print(f'O total gasto nas compras foi de R$ {total}')
print(f'{cont} Produto(s) custa(m) mais de R$1000')
print(f'O produto mais barato foi {barato} e custou R${menor}')
print('Finalizando...')
