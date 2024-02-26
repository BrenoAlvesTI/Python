def leiaint(msg):
    while True:
        try:
            n = int (input (msg))
        except (ValueError, TypeError):
            print ('\033[31mERRO! digite um número inteiro válido!\033[m')
            continue
        except KeyboardInterrupt:
            return 0
        else:
            return n

def leiaReal(msg):
    while True:
        try:
            n = float (input (msg))
        except (ValueError, TypeError):
            print ('\033[31mERRO! digite um número real válido!\033[m')
            continue
        except KeyboardInterrupt:
            return 0
        else:
            return n

i = leiaint ('Digite um número inteiro: ')
r = leiaReal ('Digite um número real: ')
print (f'Você digitou o número inteiro {i} e real {r}')

#Este programa só aceita número inteiros e reais