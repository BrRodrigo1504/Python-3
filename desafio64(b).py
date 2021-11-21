numero = cont = soma = 0

while numero != 999:
    numero = int(input('Digite algum número [999 para parar]: '))
    cont += 1
    soma += numero
print('Voce digitou {} números e a soma entre eles foi {}!!'.format(cont - 1, soma - 999))