tot18 = totH = jovem = cont = 0
print('-' * 30)
print('CADASTRE UMA PESSOA')
print('-' * 30)
while True:
    idade = int(input('Quantos anos voce tem?'))
    print('-' * 30)
    genero = ' '
    while genero not in 'MF':
        genero = str(input('Qual é o seu genero?')).strip().upper()[0]
    print('-' * 30)
    if idade >= 18:
        cont += 1
        tot18 += 1
    if genero == 'M':
        totH += 1
        cont +=1
    if genero == 'F':
        cont += 1
        if idade <= 20:
            jovem += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?')).strip().upper()[0]
    print('-' * 30)
    if resp == 'N':
        break
print(f'O total de pessoas com mais de 18 anos : {tot18}')
print(f'Ao todo temos {totH} Homem(ns) cadastrado(s)')
print(f'O total de mulheres com menos de 20 anos foi de {jovem}')


