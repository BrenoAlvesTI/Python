print ('-'*40)
print (f'{"LISTAGEM DE PRECOS":^40}')
print ('-'*40)

listagem = ("Lápis", 1.75, "Borracha", 2.80, "Caderno", 15.00, "Estojo", 25.00, "Transferidor", 4.20, "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)

for posiçao in range(0,len(listagem)):
    if posiçao % 2 == 0:
        print (f'{listagem[posiçao]:.<30}', end = '')
    else: 
        print (f'R${listagem[posiçao]:>7.2f}')
print ('-'*40)