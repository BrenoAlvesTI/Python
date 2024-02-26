def dobro(n=0):
    n = n * 2
    return n

def metade(n=0):
    n = n / 2
    return n
    
def aumento(n=0,au=0):
    a = (n * au) / 100
    n = n + a
    return n

def redução(n=0,re=0):
    r = (n * re) / 100
    n = n - r
    return n

def moeda(preço=0, moeda='R$'):
    return f"{moeda}{preço:.2f}".replace('.', ',')