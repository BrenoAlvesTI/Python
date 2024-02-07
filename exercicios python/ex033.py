v1 = int (input ('Digite o primeiro valor:'))
v2 = int (input ('Digite o segundo valor:'))
v3 = int (input ('Digite o terceiro valor:'))

mv = v1
mev = v1
if v2 > v1 and v2 > v3:
    mv = v2
if v3 > v1 and v3 > v2:
    mv = v3
if v2 < v1 and v2 < v3:
    mev = v2
if v3 < v1 and v3 < v2:
    mev = v3
    
print (f'O maior valor digitado foi {mv} e o menor foi {mev}')

# Este programa informa o maior e menor valor digitado
