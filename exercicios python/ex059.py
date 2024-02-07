from time import sleep
mn = 0
v1 = int (input ('Primeiro valor: '))
v2 = int (input ('Segundo valor: '))

sleep (1)
print ('=-='*10)
print ('[ 1 ] Somar')
print ('[ 2 ] Multiplicar')
print ('[ 3 ] Maior')
print ('[ 4 ] Novos Números')
print ('[ 5 ] Sair do Programa')
print ('=-='*10)

o = int (input ('>>>>> Qual é a sua opção? '))
while o != 5:
    
    if o == 1:
        s = v1 + v2
        sleep (1)
        print (f'A soma entre {v1} + {v2} é {s}')
        print ('=-='*10)
        print ('[ 1 ] Somar')
        print ('[ 2 ] Multiplicar')
        print ('[ 3 ] Maior')
        print ('[ 4 ] Novos Números')
        print ('[ 5 ] Sair do Programa')
        print ('=-='*10)
        o = int (input ('>>>>> Qual é a sua opção? '))
        
    elif o == 2:
        m = v1 * v2
        sleep (1)
        print (f'O resultado de {v1} X {v2} é {m}')
        print ('=-='*10)
        print ('[ 1 ] Somar')
        print ('[ 2 ] Multiplicar')
        print ('[ 3 ] Maior')
        print ('[ 4 ] Novos Números')
        print ('[ 5 ] Sair do Programa')
        print ('=-='*10)
        o = int (input ('>>>>> Qual é a sua opção? '))
        
    elif o == 3:
        if v1 > v2:
            mn = v1
            sleep (1)
            print (f'Entre {v1} e {v2} o maior valor é {mn}')
            print ('=-='*10)
            print ('[ 1 ] Somar')
            print ('[ 2 ] Multiplicar')
            print ('[ 3 ] Maior')
            print ('[ 4 ] Novos Números')
            print ('[ 5 ] Sair do Programa')
            print ('=-='*10)
            o = int (input ('>>>>> Qual é a sua opção? '))
            
        elif v1 < v2:
            mn = v2
            sleep (1)
            print (f'Entre {v1} e {v2} o maior valor é {mn}')
            print ('=-='*10)
            print ('[ 1 ] Somar')
            print ('[ 2 ] Multiplicar')
            print ('[ 3 ] Maior')
            print ('[ 4 ] Novos Números')
            print ('[ 5 ] Sair do Programa')
            print ('=-='*10)
            o = int (input ('>>>>> Qual é a sua opção? '))
            
        else:
            sleep (1)
            print ('Os valores são iguais!')
            print ('=-='*10)
            print ('[ 1 ] Somar')
            print ('[ 2 ] Multiplicar')
            print ('[ 3 ] Maior')
            print ('[ 4 ] Novos Números')
            print ('[ 5 ] Sair do Programa')
            print ('=-='*10)
            o = int (input ('>>>>> Qual é a sua opção? '))
            
    elif o == 4:
        sleep (1)
        print ('Informe os números novamente: ')
        v1 = int (input ('Primeiro valor: '))
        v2 = int (input ('Segundo valor: '))
        print ('[ 1 ] Somar')
        print ('[ 2 ] Multiplicar')
        print ('[ 3 ] Maior')
        print ('[ 4 ] Novos Números')
        print ('[ 5 ] Sair do Programa')
        o = int (input ('>>>>> Qual é a sua opção? '))
        print ('=-='*10)
        
    else:
        sleep (1)
        print ('Opção inválida. Tente Novamente!')
        print ('=-='*10)
        print ('[ 1 ] Somar')
        print ('[ 2 ] Multiplicar')
        print ('[ 3 ] Maior')
        print ('[ 4 ] Novos Números')
        print ('[ 5 ] Sair do Programa')
        print ('=-='*10)
        o = int (input ('>>>>> Qual é a sua opção? '))
        
print ('Finalizando...')
print ('=-='*10)
sleep (1)
print ('Fim do programa! Volte sempre!')

# Este Programa Analisa Números    