pessoas18 = cadastrohomem = mulheres20 = 0
while True:
    print ('-'*30)
    print ('CADASTRE UMA PESSOA')
    print ('-'*30)
    idade = int (input ('Idade: '))
    if idade >= 18:
        pessoas18 = pessoas18 + 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str (input ('Sexo: [M/F] ')).strip().upper()[0]
        if sexo == 'M':
            cadastrohomem = cadastrohomem + 1
        elif sexo == 'F' and idade <= 20:
            mulheres20 = mulheres20 + 1
    r = ' '
    while r not in 'SN':
        r = str (input ('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        print ('-'*30)
        break
print (f'há {pessoas18} pessoas com mais de 18 anos.')
print (f'{cadastrohomem} homens foram cadastrados.')
print (f'{mulheres20} mulheres tem menos de 20 anos.')