import moeda

p = float (input ('Digite o preço: R$'))
print (f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print (f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print (f'Aumentando 10% temos {moeda.aumento(p, 10, True)}')
print (f'Reduzindo 40% temos {moeda.redução(p, 40, True)}')

#Este programa utiliza módulos feitos por mim (aprimoração do ex108)