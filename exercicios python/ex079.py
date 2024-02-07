valores = list()
while True:
    valor = int (input ('Digite um valor: '))
    if valor not in valores:
        valores.append(valor)
        print ('Valor adicionado com sucesso!')
    else:
        print ('Valor duplicado! Não vou adicionar...')
    resposta = ' '
    while resposta not in 'SN':
        resposta = str (input ('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
valores.sort()
print ('=-='*15)
print (f'Você digitou os valores {valores}')
print ('=-='*15)

# Este programa guarda valores