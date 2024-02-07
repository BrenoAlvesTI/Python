resultado = 0
while True:
    numero = int (input ('Digite o número para saber a tabuada: '))
    if numero < 0:
        break
    for c in range (1,11):
        resultado = numero * c
        print (f'{numero} X {c:2} = {resultado}')
print ('Programa encerrado!')

#este programa faz a tabuada do número desejado até você escrever um número negativo