maior = 0
menor = 0
for p in range (1, 6):
    peso = float (input (f'{p}° peso:'))
    if peso == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print (f'O maior peso foi {maior}kg')
print (f'O menor peso foi {menor}kg')

# Este programa informa o maior e menor peso