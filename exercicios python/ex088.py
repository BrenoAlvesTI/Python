from random import randint
from time import sleep
print ('=-='*5, ' MEGA SENA ', '=-='*5)
total = 1
lista = list()
jogos = list()
quantosj = int (input ('Quantos jogos: '))
while total <= quantosj:
    c = 0
    while True:
        numero = randint (1,60)
        if numero not in lista:
            lista.append(numero)
            c = c + 1
        if c == 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total = total + 1
print ('=-='*20)
print (f'{'SORTEANDO...':^60}')
print ('=-='*20)
sleep(1)
for i, j in enumerate(jogos):
    print (f'Jogo {i+1}: {j}')
    sleep(1)
print ('=-='*20)
print (f'{'BOA SORTE!':^60}')
print ('=-='*20)

# Este Programa cria jogos para a Mega Sena        