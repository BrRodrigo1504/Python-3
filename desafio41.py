i = int(input('Digite a sua idade para saber a sua categoria: '))

if i<= 9:
    print('Voce pertence a categoria Mirim')
elif i <= 14:
    print('Voce pertence a categoria Infantil')
elif i <= 19:
    print('Voce pertence a categoria Junior')
elif i <= 20:
    print('Voce pertence a categoria Sênior')
elif i>=21:
    print('Voce pertence a categoria Master')