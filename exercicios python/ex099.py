from time import sleep

def maior (* n):
    print ('Analisando valores...')
    cont = maior = 0
    for v in n:
        print (f'{v} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = v
        else:
            if maior < v:
                maior = v
        cont += 1
    print ()
    print (f'Foram analisados {cont} valores.')
    print (f'O valor mais alto foi {maior}')
    print ('=-='*30)
print ('=-='*30)
maior (4,6,9,2,1,7)
maior (5,7,1)
maior (1,3)
maior ()

# Este programa analisa valores selecionados