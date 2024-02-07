from datetime import date
anonascimento = int (input ('Ano de nascimento: '))
anoatual = date.today().year
idade = anoatual - anonascimento
if idade > 0 and idade <= 9:
    print (f'O atleta tem {idade} anos')
    print ('Classificação: Mirin')
elif idade <= 14:
    print (f'O atleta tem {idade} anos')
    print ('Classificação: Infantil')
elif idade <= 19:
    print (f'O atleta tem {idade} anos')
    print ('Classificação: Junior')
elif idade <= 25:
    print (f'O atleta tem {idade} anos')
    print ('Classificação: Sênior')
else:
    print (f'O atleta tem {idade} anos')
    print ('Classificação: Master')

# Este programa informa a classe do atleta pela idade