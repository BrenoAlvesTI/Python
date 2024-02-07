print ('=-='*10)
print ('VAMOS JOGAR PAR OU ÍMPAR')
print ('=-='*10)
from random import randint
computador = randint (0,10)
total = soma = 0
while True:
    valor = int (input ('Digite um valor: '))
    soma = valor + computador
    escolha = ' '
    while escolha not in 'PI':
        escolha = str (input ('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    print ('-'*30)
    print (f'Você jogou {valor} e o computador {computador}. Total de {soma} ', end = '')
    if escolha == 'P':
        if soma % 2 == 0:
            print ('DEU PAR')
            print ('VOCÊ VENCEU!')
            total = total + 1
        else:
            print ('DEU ÍMPAR')
            print ('VOCÊ PERDEU!')
            break
    if escolha == 'I':
        if soma % 2 == 1:
            print ('DEU ÍMPAR')
            print ('VOCÊ VENCEU!')
            total = total + 1
        else:
            print ('DEU PAR')
            print ('VOCÊ PERDEU!')
            break
print ('=-='*10)
print (f'GAME OVER! Você venceu {total} vezes.')
