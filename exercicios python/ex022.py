n = str (input ('Digite seu nome completo: ')).strip()

print ('Seu nome em maiúsculas é: ')
print (n.upper())
print ('Seu nome em minúsculas é: ')
print (n.lower())
ql = (len(n)-n.count(' '))
print (f'Seu nome tem ao todo {ql} letras')
pn = n.find(' ')
print (f'Seu primeiro nome tem {pn} letras')

# Este programa diz informações sobre seu nome