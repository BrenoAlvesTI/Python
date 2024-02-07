from datetime import date
anoatual = date.today().year
temmais = 0
temenos = 0
for p in range (1, 8):
    anonascimento = int (input (f'Ano de nascimento da {p}° pesoa: '))
    idade = anoatual - anonascimento
    if idade >= 21:
        temmais = temmais + 1
    else:
        tm = tm + 1
print (f'Há {temmais} pessoas maiores de idade')
print (f'Há também {temenos} pessoas menores de idade')

# Este programa diz quantas pessoas são maiores de idade