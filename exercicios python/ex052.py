t = 0
numero = int (input ('Digite um número: '))

for c in range (1, numero + 1):
    
    if numero % c == 0:
        t = t + 1
        print ('\033[34m', end = '')
        
    else:
        print ('\033[31m', end = '')
        
    print (f'{c}', end = ' ')
    
print (f'\n\033[mO número {numero} foi divisível {t} vezes')

if t == 2:
    print ('Por isso ele é PRIMO')
else:
    print ('Por isso ele não é PRIMO')

# Este programa informa se um número é primo