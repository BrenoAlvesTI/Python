def dobro(n=0, formato=False):
    n = n * 2
    return n if formato is False else moeda(n)

def metade(n=0, formato=False):
    n = n / 2
    return n if formato is False else moeda(n)
    
def aumento(n=0,au=0, formato=False):
    a = (n * au) / 100
    n = n + a
    return n if not formato else moeda(n)

def redução(n=0,re=0, formato=False):
    r = (n * re) / 100
    n = n - r
    return n if not formato else moeda(n)

def moeda(preço=0, moeda='R$'):
    return f"{moeda}{preço:.2f}".replace('.', ',')

def titulo(msg):
    t = len(msg) + 30
    print ('=' * t)
    print (f'{msg:^43}')
    print ('=' * t)
    
def resumo(p=0, au=0, r=0):
    titulo ('RESUMO DO VALOR')
    print (f'Preço analisado:     R${moeda(p)}'.replace('.', ','))
    print (f'Dobro do preço:      R${dobro(p, True)}'.replace('.', ','))
    print (f'Metade do preço:     R${metade(p, True)}'.replace('.', ','))
    print (f'{au}% de aumento:      R${aumento(p, au, True)}'.replace('.', ','))
    print (f'{r}% de redução:      R${redução(p, r, True)}'.replace('.', ','))
    print ('=' * 45)
    
    