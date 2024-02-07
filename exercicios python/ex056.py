hmv = 0
somaidade = 0
menosde20 = 0
mediaidade = 0
nomemaisvelho = ''

for p in range (1, 5):
    
    print (f'-----{p}° pessoa-----')
    nome = str (input (f'{p}° nome: ')).capitalize()
    idade = int (input ('Idade: '))
    sexo = str (input ('Sexo: [M/F] '))
    
    somaidade = somaidade + idade
    mediaidade = somaidade / 4
    
    if p == 1 and sexo in 'Mm':
        hmv = idade
        nomemaisvelho = nome
        
    elif idade > hmv and sexo in 'Mm':
        hmv = idade
        nomemaisvelho = nome
        
    elif idade < 20 and sexo in 'Ff':
        menosde20 = menosde20 + 1
        
print (f'A média das idades é {mediaidade:.1f}')
print (f'A idade do homem mais velho é {hmv} e o nome é {nomemaisvelho}')
print (f'E há {menosde20} mulheres com menos de 20 anos')

# Este programa analisa pessoas