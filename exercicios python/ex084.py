pessoas = list()
dados = list()
maiorpeso = menorpeso = 0
resposta = ' '
while True:
    dados.append(str (input ('Nome: ')))
    dados.append(float (input ('Peso: ')))
    if len(pessoas) == 0:
        maiorpeso = menorpeso = dados[1]
    else:
        if dados[1] > maiorpeso:
            maiorpeso = dados[1]
        elif dados[1] < menorpeso:
            menorpeso = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resposta = str (input ('Quer continuar? [S/N] ')).strip().upper()[0]
    while resposta not in 'SN':
        resposta = str (input ('Quer continuar? [S/N]')).strip().upper()[0]
    if resposta == 'N':
        break
print ('=-='*20)
print (f'O total de pessoas cadastradas é {len(pessoas)}')
print (f'O maior peso foi de {maiorpeso}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maiorpeso:
        print (f'[{p[0]}] ', end='')
print ()
print (f'O menor peso foi de {menorpeso}kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menorpeso:
        print (f'[{p[0]}] ', end='')
print ()
print ('=-='*20)

# Este programa analisa pesos