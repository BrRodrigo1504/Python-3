from math import sqrt
n1=float(input('Comprimento do cateto oposto: '))
n2=float(input('Comprimento do cateto adjacente: '))
h=(n1**2)+(n2**2)
print('A hipotenusa vale {:.2f}'.format(sqrt(h)))