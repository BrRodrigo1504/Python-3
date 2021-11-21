n = input('Seu nome completo: ')
n0 = float(input('Digite o seu salario:'))
n2 = float(input('Qual o valor total financiado?'))
n3 = int(input('Em quantos anos deseja pagar?'))
parcela = n2/(n3*12)
print('Estamos analisando o seu requerimento, aguarde...')
if parcela>=(n0*0.3):
    print('Seu requerimento não foi aprovado, ele excede os 30% do seu salário')
else:
    print('O valor de cada parcela será de : {:.2f} euros'.format(parcela))





