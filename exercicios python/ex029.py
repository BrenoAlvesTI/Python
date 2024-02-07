velocidade = int (input ('Qual é a velocidade atual do carro? '))
m = (velocidade-80) * 7
if velocidade > 80:
    print ('MULTADO! Você excedeu o limite permitido de 80km/h')
    print (f'Você deve pagar uma multa de R${m}!')
    print ('Tenha um bom dia! Dirija com segurança!')
else:
    print ('Tenha um bom dia! Dirija com segurança!')

# Este programa analisa multas de velocidade