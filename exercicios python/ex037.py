n = int (input ('Digite um número inteiro: '))

print ('''escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')

opçao = int (input ('Sua opção: '))
if opçao == 1:
    print ('{} convertido para BINÁRIO é igual a {}'.format(n,bin(n)[2:]))
elif opçao == 2:
    print ('{} convertido para OCTAL é igual a {}'.format(n,oct(n)[2:]))
elif opçao == 3:
    print ('{} convertido para HEXADECIMAL é igual a {}'.format(n,hex(n)[2:]))
else:
    print ('''OPÇÃO INVÁLIDA
TENTE NOVAMENTE!''')

#este programa converte um número inteiro para binário, octal ou hexadecimal
