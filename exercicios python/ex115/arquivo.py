from módulos import *

def arquivoE(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarA(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print ('\033[31mHouve um erro na criação do arquivo!\033[m')
    else:
        print (f'\033[32mArquivo {nome} criado com sucesso!\033[m')
        
def lerA(nome):
    try:
        a = open(nome, 'rt')
    except:
        print ('\033[31mErro ao abrir o arquivo!\033[m')
    else:
        título('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()
        
def cadastrar(arq, nome = 'desconhecido', idade = 0):
    try:
        a = open(arq, 'at')
    except:
        print ('\033[31mHouve um erro na abertura do arquivo!\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print ('\033[31mHouve um erro na hora de abrir os dados!\033[m')
        else:
            print (f'\033[32mNovo registro de {nome} realizado com sucesso!\033[m')
            a.close()