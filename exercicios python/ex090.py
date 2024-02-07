aluno = dict()
aluno['nome'] = str (input ('Nome? '))
aluno['média'] = float (input (f'Média de {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
for k, v in aluno.items():
    print (f'{k} é igual a {v}.')
    
# Este programa analisa a situação do aluno usando dicionários