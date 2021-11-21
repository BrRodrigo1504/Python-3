palavras = ('azeite', 'cachorro', 'bolo', 'estrgonofe',
            'arroz', 'batata', 'python', 'programador',
            'trabalhar', 'mercado', 'curso', 'estudar')


for p in palavras:
    print(f'\nNa palavra {p} temos : ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra,end=' ')