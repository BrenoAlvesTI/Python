termo = int (input ('Primeiro Termo: '))
razao = int (input ('Razão: '))
d = termo + (10 - 1) * razao
for c in range (termo, d + razao, razao):
    print (f'{c} ', end=' - ')
print ('ACABOU')

# Este programa conta de acordo com suas escolhas