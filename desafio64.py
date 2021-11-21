numero = cont = soma = 0
numero = int(input('Digite algum número [999 para parar]: '))
while numero != 999:
    cont += 1
    soma += numero
    numero = int(input('Digite algum número [999 para parar]: '))
print('Voce digitou {} números e a soma entre eles foi {}!!'.format(cont, soma))