n1 = float(input('Digite a nota do seu primeiro período: '))
n2 = float(input('Digite a nota do seu segundo período : '))
m = (n1+n2)/2

if m<=4.9:
    print('\033[4;31mA sua média foi {}, Voce foi Reprovado!!'.format(m))
elif m<=5:
    print('\033[4;31mA sua média foi {}, Voce está de Recuperação!!'.format(m))
elif m>=7:
    print('\033[4;36mA sua média foi {}, Voce foi Aprovado!!Parabens!!'.format(m))
