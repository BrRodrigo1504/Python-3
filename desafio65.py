resp = 'S'
media = cont = soma = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um número: '))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
media = soma / cont
print('A media de todos os {} valores foi de {} '.format(cont, media))
print('O maior valor foi {} e o menor valor foi {} '.format(maior, menor))
print('Finalizando...')