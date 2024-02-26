from módulos import *
from arquivo import *
from time import sleep

arq = 'pessoas.txt'

if not arquivoE(arq):
    criarA(arq)
    
while True:
    resposta = menu (['Ver pessoas cadastradas', 'Cadastrar pessoas', 'Sair do sistema'])
    if resposta == 1:
        lerA(arq)
    elif resposta == 2:
        título('NOVO CADASTRO')
        nome = str (input ('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        print ('SAINDO DO PROGRAMA... ATÉ MAIS!')
        break
    else:
        print ('\033[31mERRO! digite um número inteiro válido!\033[m')
    sleep (1)
    
#Este programa cadastra pessoas