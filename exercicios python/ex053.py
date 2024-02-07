frase = str (input ('Digite uma frase ou nome: ')).strip().upper()
p = frase.split()
j = ''.join(p)
i = ''
for l in range (len(j)-1, -1, -1):    # Outro calculo mais simples do inverso é da seguinte forma: i = j[::-1]
    i = i + (j[l])
print (f'O inverso de {j} é {i}')
if i == j:
    print ('Temos um palíndromo')
else:
    print ('Não temos um palíndromo')

# Este programa informa se a frase ou palavra é um palíndromo