print('Gerador de PA')
print('-=-' * 20)
primeiro = int(input('Digite o primeiro termo da PA: '))
razão = int(input('Digite a razão da PA:'))
termo = primeiro
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print('{} » '.format(termo), end='')
        termo += razão
        cont += 1
    print('Pausa')
    mais = int(input('Quantas razões voce quer a mais?'))
print('Finalizando....')
