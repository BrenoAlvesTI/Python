import moeda

p = float (input ('Digite o preço: R$'))
print (f'A metade de {p} é {moeda.metade(p):.2f}')
print (f'O dobro de {p} é {moeda.dobro(p):.2f}')
print (f'Aumentando 10% temos {moeda.aumento(p, 10):.2f}')
print (f'Reduzindo 40% temos {moeda.redução(p, 40):.2f}')

#Este programa utiliza módulos feitos por mim