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