distancia = int (input ('Qual é a distância da sua viagem? (em km) '))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print (f'Você está prestes a começar uma viagem de {distancia} km.')
print (f'O preço da sua passagem será de R${preco:.2f}')

# Este programa calculo o preço de uma viagem