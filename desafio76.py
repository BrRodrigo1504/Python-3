lista = ('Lápis', 1.75,
         'Borracha', 2,
         'Caderno', 12.90,
         'Estojo', 25,
         'Trasnferidor', 4.20,
         'Compasso', 4.79,
         'Mochila', 124.99,
         'Canetas', 22.90,
         'Livro', 49.99,)
print('-' * 40 )
print(f'            LISTA DE PREÇOS')
print('-' * 40 )
for pos in range(0, len(lista)):
    if pos % 2 == 0:
       print(f'{lista[pos]:.<30}',end='')
    else:
        print(f'R${lista[pos]:>6.2f}')
