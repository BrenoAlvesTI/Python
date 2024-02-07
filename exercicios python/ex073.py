brasileirao = ("Flamengo", "Palmeiras", "Atlético Mineiro", "Grêmio", "São Paulo", "Internacional", "Fluminense", "Athletico Paranaense", "Corinthians", "Cruzeiro", "Vasco da Gama", "Botafogo", "Bahia", "Santos", "Sport Recife", "Chapecoense", "Ceará", "Fortaleza", "Goiás", "América Mineiro")
print (f'Lista de times do Brasileirão: {brasileirao}')
print ('-'*145)
print (f'Os 5 primeiros são: {brasileirao[0:5]}')
print ('-'*145)
print (f'Os 4 últimos são: {brasileirao[16:]}')
print ('-'*145)
print (f'Times em ordem alfabética: {sorted(brasileirao)}', end = '')
print ('-'*145)
c = brasileirao.index ('Chapecoense')
print (f'Chapecoense está na {c+1}° posição')
print ('-'*145)

#Este programa analisa a tabela do brasileirão