resposta = str (input ('Digite seu sexo: [M/F] ')).strip().upper()[0]
while resposta not in 'MF':
    resposta = str (input ('Resposta inválida! Por favor Informe seu Sexo: ')).strip().upper()[0]
print (f'Sexo {resposta} registrado com sucesso!')

# Este programa registra seu sexoprint ('-='*10)