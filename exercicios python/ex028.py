import random
r = random.randint(0,3)
resposta = int (input ('Em que número estou pensando? '))
if resposta == r:
    print ('Parabéns! você acertou!')
else:
    print ('Você errou :(')

# Este programa diz se você acerou o número que ele está pensando