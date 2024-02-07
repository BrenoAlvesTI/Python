print ('-='*10)
print ('SEQUÊNCIA DE FIBONACCI')
print ('-='*10)
t = int (input ('Quantos termos você quer mostrar? '))
c = 1
n1 = 0
n2 = 1
n3 = 0
print (f'{n1} > {n2} > ', end = '')
while c <= t - 2:
    n3 = n1 + n2
    print (f'{n3} > ', end = '')
    n1 = n2
    n2 = n3
    c = c + 1
print ('Fim')

# Este programa mostra a sequência de fibonnaci