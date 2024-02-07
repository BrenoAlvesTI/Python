valores = list()
total = 0
resposta = ' '
while True:
    valor = int (input ('Digite um valor: '))
    valores.append(valor)
    total = total + 1
    resposta = str (input ('Quer continuar? [S/N] ')).strip().upper()[0]
    while resposta not in 'SN':
        resposta = str (input ('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print ('=-='*20)
valores.sort(reverse=True)
print (f'Você digitou {total} elementos')
print (f'Os elementos em ordem decrescente são: {valores}')
if 5 in valores:
    print ('O valor 5 faz parte da lista!')
else:
    print ('O valor 5 não faz parte da lista!')
print ('=-='*20)

# Este programa analisa números