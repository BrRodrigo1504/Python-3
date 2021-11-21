a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
if a>b and a>c:
    print('{} é o maior valor'.format(a))
if b>a and b>c:
    print('{} é o maior valor'.format(b))
if c>a and c>b:
    print('{} é o maior valor'.format(c))
if a<b and a<c:
    print('{} é o menor valor'.format(a))
if b<a and b<c:
    print('{} é o menor valor'.format(b))
if c<a and c<b:
    print('{} é o menor valor'.format(c))

