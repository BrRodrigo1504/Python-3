a = int(input('Digite um ano qualquer?'))
b = a % 4
if b==0:
    print('O ano {} é Bissexto!!'.format(a))
else:
    print('O ano {} não é Bissexto'.format(a))