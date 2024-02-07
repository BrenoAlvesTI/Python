numero = int (input ('Digite um número para calcular seu fatorial: '))
c = 0
fatorial = 1
print ('=-='*10)
for c in range(numero, 0, -1):
        print (f' {c} ', end='')
        fatorial = fatorial * c
        print ('x' if c > 1 else '= ', end='')
print (f'{fatorial}', end='')
print ()
print ('=-='*10)

# Este programa calcula o fatorial de um número
# Tem a forma sem módulo acima e com módulo abaixo

('''from math import factorial
n = int (input ('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print ('=-='*5)
print(f)
print ('=-='*5)''')