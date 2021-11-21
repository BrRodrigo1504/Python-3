p = float(input('Digite o valor a ser pago: '))
print(''' Formas de Pagamento:
[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista no cartão
[ 3 ] Em até 2x no cartão
[ 4 ] 3x ou mais no cartão''')
e = int(input('Qual a opção desejada: '))
if e == 1:
    total = p*0.9
elif e == 2:
    total = p*0.95
elif e == 3:
    total = p
    parcela = total/2
    print('Sua compra será parcelado em 2x de R${:.2f}'.format(parcela))
elif e == 4:
    total = p*1.2
print('Sua compra de R${:.2f} vai custar R${:.2f} no final!'.format(p, total))
