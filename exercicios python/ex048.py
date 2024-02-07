somaimpar = 0
contador = 0
for c in range (1,501, 2):
    if c % 3 == 0:
        co = co + 1
        somaimpar = somaimpar + c
print (f'A soma de todos os {contador} valores solicitados é {somaimpar}')

# Este programa faz a soma de todos os números ímpares multiplos de 3