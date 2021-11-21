r1 = int(input('Tamanho da primeira reta'))
r2= int(input('Tamanho da segunda reta'))
r3 = int(input('Tamanho da terceira reta'))
if r1+r2>r3 and r1+r3>r2 and r2+r3>r1:
    print('As retas conseguem formar um triangulo')
else:
    print('As retas não conseguem formar um triangulo')