from random import randint

print ('''Sou seu Computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')

total = 0
computador = randint (0,10)
a = False

while not a:
    
    resposta = int (input ('Qual é seu palpite? '))
    
    if resposta == computador:
        total = total + 1
        a = True
        
    elif resposta < computador:
        print ('Mais... Tente Novamente!')
        total = total + 1
        
    else:
        print ('Menos... Tente Novamente!')
        total = total + 1
        
print (f'Parabéns! Você ganhou com {total} tentativas.')

# Este prgrama te desafia a adivinhar um número de 0 a 10