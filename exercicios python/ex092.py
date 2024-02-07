from datetime import date
ano = date.today().year
dados = {}
dados['nome'] = str (input ('Nome: '))
nascimento = int (input ('Ano de Nascimento: '))
dados['idade'] = date.today().year - nascimento
dados['C.Trabalho'] = int (input ('Carteira de Trabalho (0 não tem): '))
if dados['C.Trabalho'] == 0:
    for k, v in dados.items():
        print (f'{k} tem o valor de {v}')
else:
    dados['A.Contrato'] = int (input ('Ano de Contratação: '))
    dados['salário'] = float (input ('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + dados['A.Contrato'] + 35 - date.today().year
print ('=-='*20)
for k, v in dados.items():
    print (f' - {k} tem o valor {v}')
print ('=-='*20)

# Este programa analisa uma pessoa