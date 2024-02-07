pt = int (input ('Primeiro termo: '))
razao = int (input ('Razão: '))

c = 1
total = 0
m = 10

while m != 0:
    total = total + m
    while c <= total:
        print (f'{pt} > ', end = '')
        pt = pt + razao
        c = c + 1
    print ('Pausa')
    print ('=-='*10)
    m = int (input ('Quantos termos você quer a mais? '))
    
print (f'Total de termos {total}')
print ('Fim')

# Este programa é uma melhoria do programa 61