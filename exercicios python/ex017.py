import math
print ('='*5,"DESAFIO 17",'='*5)
co = float (input ('Digite o cateto oposto: '))
ca = float (input ('Digite o cateto adjacente: '))
h = math.hypot(co,ca)
print (f'A hipotenusa vai medir: {h:.2f}')

# Este programa calcula a hipotenusa de um triângulo