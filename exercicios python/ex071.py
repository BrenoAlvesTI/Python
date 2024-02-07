print ('-='*10)
print ('BEM VINDO AO BANCO CEV!')
print ('-='*10)
valortotal = float (input ('Quanto você quer sacar? '))
totalcedulas = 0
cedula = 50
while True:
    if valortotal >= cedula:
        valortotal = valortotal - cedula
        totalcedulas = totalcedulas + 1
    else:
        if totalcedulas > 0:
            print (f'Total de {totalcedulas} cédulas de R${cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totalcedula = 0
        if valortotal == 0:
            print ('-='*25)
            break
print ('TRANSAÇÂO FINALIZADA, VOLTE SEMPRE AO BANCO CEV!')
print ('-='*25)

# Este programa é um caixa eletrônico