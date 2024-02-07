pessoa = dict()
galera = list()

soma = média = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str (input ('Nome: '))
    while True:
        pessoa["sexo"] = str (input ('Sexo: [M/F] ')).strip().upper()[0]
        if pessoa["sexo"] in 'MF':
            break
        print ("ERRO! Digite apenas M ou F.")
    pessoa['idade'] = int (input ('Idade: '))
    soma = soma + pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resposta = str (input ('Quer continuar? [S/N]')).strip().upper()[0]
        if resposta in 'SN':
            break
        print ("ERRO! Digite apenas S ou N")
    if resposta == 'N':
        break
print ('=-='*30)
print (f'A) Ao todo temos {len(galera)} pessoas cadastradas.')
média = soma / len(galera)
print (f'B) A média de idade é de {média:.2f} anos')
print ('C) As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print (f'{p["nome"]} ', end='')
print()
print ('D) Lista de pessoas que estão acima da média: ')
for p in galera:
    if p["idade"] > média:
        for k, v in p.items():
            print (f'{k} = {v}; ', end='')
print ()
print ("Progama Finalizado!")
print ('=-='*30)

# Este programa analisa dados de pessoas