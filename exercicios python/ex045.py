from random import randint
from time import sleep
items = ('pedra','papel','tesoura')
computador = randint(0, 2)
print ('''OPÇÕES:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogada = int (input ('Qual é a sua jogada? '))
print ('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print ('-='*5)
print ('Computador jogou {}'.format(items[computador]))
print ('Jogador jogou {}'.format(items[jogada]))
print ('-='*5)
if computador == 0:
    if jogada == 0:
        print ('EMPATE!!!')
    if jogada == 1:
        print ('JOGADOR GANHOU!')
    if jogada == 2:
        print ('COMPUTADOR GANHOU!')
elif computador == 1:
    if jogada == 0:
        print ('COMPUTADOR GANHOU!')
    if jogada == 1:
        print ('EMPATE!!!')
    if jogada == 2:
        print ('JOGADOR GANHOU!')
elif computador == 2:
    if jogada == 0:
        print ('JOGADOR GANHOU!')
    if jogada == 1:
        print ('COMPUTADOR GANHOU!')
    if jogada == 2:
        print ('EMPATE!!!')

# Este programa joga JOKENPO com você