time = []
jogador = {}
partidas = []

while True:
    jogador.clear()
    jogador['nome'] = str (input ('Nome: '))
    total = int (input (f'Quantas partidas {jogador['nome']} jogou? '))
    partidas.clear()
    for c in range(0,total):
        partidas.append (int (input (f'Quantos gols {jogador['nome']} fez na {c+1}° partida? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resposta = str (input ('Quer continuar? [S/N] ')).strip().upper()[0]
        if resposta in 'SN':
            break
        print ('ERRO! digite S ou N.')
    if resposta == 'N':
        break
print ('=-='*25)
print ('cod ', end='')
for i in jogador.keys():
    print (f' {i:<15} ', end='')
print ()
print ('=-='*25)
for k, v in enumerate(time):
    print (f'{k:>3} ', end='')
    for d in v.values():
        print (f'{str(d):<15}', end='')
    print ()
print ('=-='*25)
while True:
    busca = int (input ('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print (f'ERRO! não existe jogador com código {busca}!')
    else:
        print (f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}: ')
        for i, g in enumerate(time[busca]["gols"]):
            print (f'    No jogo {i+1} fez {g} gols')
    print ('=-='*25)
    
# Este programa analisa vários jogadores