def linha(t = 40):
    return '=' * t

def título(msg):
    print(linha())
    print (msg.center(40))
    print(linha()) 

def leiaInt(msg):
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

def menu(lista):
    título('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print (f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print (linha())
    opc = leiaInt('\033[32mSua Opção:\033[m ')
    return opc