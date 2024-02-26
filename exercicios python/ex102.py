def fatorial(n, show=False):
    """
    --> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostra ou não a conta.
    :param return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print (c, end='')        
            if c > 1:
                print (' x ', end ='')
            else:
                print (' = ', end='')
        f *= c
    return f

num = int (input ('Digite o número para saber o fatorial: '))
print ('=-='*25)
print (fatorial (num, show=True))

#Este programa calcula o fatorial de um número