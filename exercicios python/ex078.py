valores = list()
maiorvalor = menorvalor = 0
for contador in range (1,6):
    valor = int (input (f'Digite um valor para a posição {contador}: '))
    valores.append(valor)
    if contador == 1:
        maiorvalor = valor
        menorvalor = valor
    else:
        if maiorvalor < valor:
            maiorvalor = valor
        elif menorvalor > valor:
            menorvalor = valor
print ('=-='*15)
print (f'Você digitou os valores {valores}')
print (f'O maior valor foi {maiorvalor} nas posições ', end = '')
for i, v in enumerate(valores):
    if v == maiorvalor:
        print (f'{i+1}... ', end = '')
print ()
print (f'O menor valor foi {menorvalor} nas posições ', end = '')
for i, v in enumerate(valores):
    if v == menorvalor:
        print (f'{i+1}... ', end = '')
        
# Este programa analisa valores