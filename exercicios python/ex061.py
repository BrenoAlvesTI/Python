pt = int (input ('Primeiro termo: '))
razao = int (input ('Razão: '))
c = 1

while c <= 10:
    print (f'{pt} > ', end = '')
    pt = pt + razao
    c = c + 1
print ('=-='*25)   
print ('Fim')
print ('=-='*25)

#Este programa faz uma contagem personalizada de 10 números