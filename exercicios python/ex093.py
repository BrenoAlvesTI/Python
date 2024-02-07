jogador = {}
partidas = []
jogador['nome'] = str (input ('Nome: '))
total = int (input (f'Quantas partidas {jogador['nome']} jogou? '))
for c in range(0,total):
    partidas.append (int (input (f'Quantos gols {jogador['nome']} fez na {c+1}° partida? ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print ('=-='*20)
print (jogador)
print ('=-='*20)
for k, v in jogador.items():
    print (f'O campo {k} tem o valor {v}')
print ('=-='*20)
print (f'O jogador {jogador['nome']} jogou {total} partidas.')
for i, g in enumerate(partidas):
    print (f' => Na partida {i+1}, fez {g} gols.')
print (f'Foi um total de {jogador['total']} gols.')
print ('=-='*20)

# Este programa analisa um jogador