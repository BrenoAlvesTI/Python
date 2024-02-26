print ('LOJA SUPER BARATÂO')
print ('-='*10)
total = acimademil = pmaisbarato = vmaisbarato = contador = 0
while True:
    nome = str (input ('Nome do produto: ')).strip().title()
    preço = float (input ('Preço: R$'))
    contador = contador + 1
    total = total + preço
    if preço > 1000:
        acimademil = acimademil + 1
    if contador == 1:
        pmaisbarato = nome
        vmaisbarato = preço
    else:
        if vmaisbarato > preço:
            vmaisbarato = preço
            pmaisbarato = nome
    resposta = ' '
    while resposta not in 'SN':
        resposta = str (input ('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        print ('=-='*15)
        break
print ('----------FIM DO PROGRAMA----------')
print ('=-='*15)
print (f'O total da compra foi R${total:.2f}')
print (f'Temos {acimademil} produtos custando mais de R$1.000')
print (f'O produto mais barato foi {pmaisbarato} que custa R${vmaisbarato:.2f}')
print ('=-='*15)

# Este programa simula uma loja