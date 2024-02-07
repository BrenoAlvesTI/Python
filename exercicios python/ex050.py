somapares = 0
contador = 0
for c in range (1,7):
    numero = int (input ('Digite um número: '))
    if numero % 2 == 0:
        somapares = somapares + numero
        contador = contador + 1
print (f'Você informou {contador} números pares e a soma dos números pares é: {somapares}')

# Este programa faz a soma dos números pares