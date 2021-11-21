i = int(input('Digite o ano que voce nasceu: '))
a = 2020-i
b = a-18
c = 18-a
d = c*12
if a<18:
    print('Você terá que se alistar em {} meses!!'.format(d))
elif a== 18:
    print('Você terá que se alistar no serviço militar esse ano!!')
elif a>= 19:
    print('Tem {} ano(s) que voce se alistou!!'.format(b))