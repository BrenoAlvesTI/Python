alunos = list()
resposta = ' '
media = 0
while True:
    nome = (str (input ('Nome: ')))
    nota1 = (float (input ('Nota 1: ')))
    nota2 = (float (input ('Nota 2: ')))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    resposta = str (input ('Quer continuar? ')).strip().upper()[0]
    while resposta not in 'SN':
        resposta = str (input ('Quer continuar? ')).strip().upper()[0]
    if resposta == 'N':
        break
print ('=-='*20)
print (f'{'N°':<4}{'NOME':<8}{'MÉDIA':>10}')
print ('-'*60)
for i, a in enumerate(alunos):
    print (f'{i:<2}{a[0]:>8}{a[2]:>10}')
print ('-'*60)
while True:
    opçao = int (input ('Digite o número do aluno para ver as notas: [999] para parar '))
    if opçao == 999:
        break
    if opçao <= len(alunos):
        print (f'As notas de {alunos[opçao][0]} são {alunos[opçao][1]}')
        print ('-'*60)
print ('=-='*20)
print (f'{'FINALIZANDO...':^20}')
print('=-='*20)

# Este Programa analisa notas