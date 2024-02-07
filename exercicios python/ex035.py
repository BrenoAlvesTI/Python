v1 = float (input ('Digite o primeiro segmento: '))
v2 = float (input ('Digite o segundo segmento: '))
v3 = float (input ('Digite o terceiro segmento: '))

if v1 < v2 + v3 and v2 < v1 + v3 and v3 < v1 + v2:
    print ('Os segmentos acima PODEM formar um triângulo!')
else:
    print ('Os segmentos acima NÃO podem formar um triângulo!')

# Este programa informa se os segmentos podem formar um triângulo
