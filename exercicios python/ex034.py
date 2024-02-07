s = float (input ('Qual é o atual salário do funcionário? R$ '))
if s <= 1250:
    s = s + (s * 15 / 100)
else:
    s = s + (s * 10 / 100) 
print (f'Seu novo salário é: R${s:.2f}')

# Este programa Informa o salário com aumento de acordo com quanto você ganha