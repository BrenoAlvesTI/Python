def notas(*n, sit=False):
    d = dict()
    d['total'] = len(n)
    d['maior'] = max(n)
    d['menor'] = min(n)
    d['média'] = sum(n)/len(n)
    
    if sit:
        if d['média'] >= 7:
            d['situaação'] = 'BOA'
        elif d['média'] >= 5:
            d['situação'] = 'RAZOAVEL'
        else:
            d['situação'] = 'RUIM'
    return d

resp = notas(7,6.4,3.7,5,2, sit=True)
print (resp)

#Este programa analisa notas