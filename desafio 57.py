genero = str(input('Informe o seu gênero: [M/F] ')).strip().upper()
while genero not in 'MF':
    genero = str(input('Dados invalidos.Por favor, informe o seu gênero: ')).strip().upper()[0]
print('\033[32mOs seus dados foram inseridos com sucesso!!')