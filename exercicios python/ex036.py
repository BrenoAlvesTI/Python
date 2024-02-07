valor = float (input ('Valor da casa: R$ '))
salario = float (input ('Salário do comprador: R$ '))
anos = int (input ('Quantos anos de financiamento? '))

preco = valor / (anos * 12)
salario30 = salario * 30 / 100
if preco > salario30:
    
    print ('Empréstimo NEGADO!')
    print (f'Para pagar uma casa de R${valor:.2f} em {anos} anos a prestação será de {preco:.2f}')
    print (f'30% do seu salário é R${salario30}')
else:
    print ('Empréstimo APROVADO!')
    print (f'Para pagar uma casa de R${valor:.2f} em {anos} anos a prestação será de {preco:.2f}')
    print (f'30% do seu salário é R${salario30}')

# Este programa informa se seu empréstimo foi aprovado ou não