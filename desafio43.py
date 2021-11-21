a = float(input('Qual o seu peso?'))
b = float(input('Qual é a sua altura?'))
c = b**2
d = a/c
if d<18.5:
    print('Voce está abaixo do peso!')
elif  18.6 <= d <25:
    print('Você está no peso ideal!')
elif  25.1<= d < 30:
    print('Você está com sobrepeso!')
elif 30.1<= d < 40:
    print('Você está obeso!')
elif d>=40:
    print('Você está com Obesidade Mórbida!')

print('O seu imc vale {}'.format(d))