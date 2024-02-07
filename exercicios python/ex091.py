from random import randint
from operator import itemgetter
from time import sleep
jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)}
raking = ()
print ('Valores Sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v}')
    sleep(1)
print ('=-='*20)
print ('  == RANKING DOS JOGADORES ==')
print ('=-='*20)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for k, v in enumerate(ranking):
    print (f' {k+1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)
print ('=-='*20)

# Este programa sorteia números