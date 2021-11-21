d = float(input('Qual a distancia da viagem?'))
p = (d/2)
p2 = (d*0.45)
if d>=201:
    print('O custo da sua viagem será de {} reais'.format(p2))
else:
    print('O custo da sua viagem será de {} reais'.format(p))