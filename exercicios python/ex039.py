from datetime import date
anoatual = date.today().year
anonascimento = int (input ('Ano de nascimento: '))
idade = anoatual - anonascimento
print (f'Quem nasceu em {anonascimento} tem {idade} em {anoatual}')
if idade == 18:
    print ('Você deve se alistar IMEDIATAMENTE!')
elif idade > 18:
    anos = idade - 18
    alistamento = anoatual - anos
    print (f'Você já deveria ter se alistado há {anos} anos')
    print (f'Seu alistamento foi em {alistamento}')
elif idade < 18:
    anos = 18 - idade
    alistamento = anoatual + anos
    print (f'Ainda faltam {anos} anos para o alistamento')
    print (f'Seu alistamento será em {alistamento}')

# Este programa analisa seu alistamento militar