numeros = [[], []]
for c in range (1, 8):
    valor = int (input (f'Digite o {c}° valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
print ('=-='*20)
numeros[0].sort()
numeros[1].sort()
print (f'Os valores pares são: {numeros[0]}')
print (f'Os números ìmpares são: {numeros[1]}')
print ('=-='*20)

# este programa separa os números pares e ìmpares