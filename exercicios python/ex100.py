from random import randint

num = []
def sorteio(* n):
    print ('Sorteando 5 valores da lista: ', end='')
    for c in range (1,6):
        r = randint(1,9)
        print (f'{r} ', end='')
        num.append(r)
    print ('PRONTO!')
def par(* nu):
    somap = 0
    for c, v in enumerate(num):
        if v % 2 == 0:
            somap += v
    print (f'Somando os valores pares de {num}, temos {somap}')
sorteio()
par()

# Este programa soma os números pares de uma lista aleatória