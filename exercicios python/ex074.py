from random import randint
n = (randint (1,10), randint (1,10), randint (1,10), randint (1,10), randint (1,10), )
print (f'Os números sorteados foram: ', end = '')
for c in n:
    print (f'{c} ', end = '')
print (f'\nO maior valor foi: {max(n)}')
print (f'O menor valor foi: {min(n)}')

# Este programa analisa números de 1-10