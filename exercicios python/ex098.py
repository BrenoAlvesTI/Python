from time import sleep

def contador(i,f,p):
    if i < f:
        if p < 0:
            p *= -1
        print ('=-='*30)
        print (f'Iniciando contagem de {i} a {f} de {p} em {p}')
        cont = i
        while cont <= f:
            print (f'{cont} ', end='', flush=True)
            sleep (0.5)
            cont += p
        print ('FIM!')
        print ('=-='*30)
    if i > f:
        print (f'Iniciando contagem de {i} a {f} de {p} em {p}')
        cont = i
        while cont >= f:
            print (f'{cont} ', end='', flush=True)
            sleep (0.5)
            cont -= p
        print ('FIM!')
        print ('=-='*30)

contador (1,10,1)
contador (10,1,1)
print ('Agora é sua vez de criar a contagem!')
ini = int (input ('Início: '))
fim = int (input ('Fim: '))
while True:
    passo = int (input ('Passo: '))
    if passo != 0:
        break
    print ('ERRO! o número 0 não pode ser o passo, Tente novamente!')
contador (ini,fim,passo)

# Este programa é um contador personalizado