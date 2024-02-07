n1 = float (input ('Primeira nota: '))
n2 = float (input ('Segunda nota: '))
media = (n1 + n2) / 2
if media >= 7:
    print (f'Sua média é {media}')
    print ('Aluno aprovado!')
elif media >= 5 and media < 7:
    print (f'Sua média é {media}')
    print ('Aluno em recuperação!')
else:
    print (f'Sua média é {media}')
    print ('Aluno reprovado!')

# Este programa analisa a situação escolar do aluno