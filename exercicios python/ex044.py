print ('-----Loja Guanabara-----')

preço = float (input ('Preço das compras: '))

print ('''FORMAS DE PAGAMENTO
[ 1 ] á vista no dinheiro / cheque
[ 2 ] á vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')

opçao = int (input ('qual é a opção? '))

if opçao == 1:
    preçodisconto = preço - preço * 10 / 100
    print (f'Sua compra de {preço:.2f} vai custar {preçodisconto:.2f} com desconto')
    
elif opçao == 2:
    preçodisconto = preço - preço * 5 / 100
    print (f'Sua compra de {preço:.2f} vai custar {preçodisconto:.2f} com desconto')
    
elif opçao == 3:
    print (f'Sua compra foi {preço:.2f}')
    
elif opçao == 4:
    parcelas = int (input ('Quantas parcelas? '))
    juros = preço * 20 / 100
    preçojuros = preço + juros
    parcelasjuros = preçojuros / parcelas
    print (f'Sua compra será parcelada em {parcelas}x de R${parcelasjuros:.2f} com juros')
    print (f'Sua compra de {preço:.2f} vai custar {preçojuros:.2f}')
    
else:
    print ('Opção inválida, tente novamente!')

# Este programa analisa formas de pagamento