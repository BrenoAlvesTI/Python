valores = list()
resposta = ' '
while True:
    valor = int (input ('Digite um valor: '))
    valores.append(valor)
    resposta = str (input ('Quer continuar? [S/N] ')).strip().upper()[0]
    while resposta not in 'SN':
        resposta = str (input ('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print ('=-='*20)
valores.sort()
print (f'Os valores digitados foram: {valores}')
print (f'Os valores pares digitados foram: ', end = '')
for pos, v in enumerate(valores):
    if v % 2 == 0:
        print (f'{valores[pos]} ', end = '')
print ()
print ('Os valores ìmpares digitados foram: ', end = '')
for pos, v in enumerate(valores):
    if v % 2 == 1:
        print (f'{valores[pos]} ', end = '')
print ()
print ('=-='*20)

# Este programa identifica os números pares e ìmpares de uma lista