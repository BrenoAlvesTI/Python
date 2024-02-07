palavras = ('Computador', 'Notebook', 'Mouse', 'Teclado', 'Carregador', 'Celular', 'Impressora', 'Internet', 'Sites', 'Jogos', 'Apps', 'Energia')

for p in palavras:
    print (f'\nNa palavra {p.upper()} temos as vogais: ', end = '')
    for letras in p:
        if letras.lower() in 'aeiou':
            print (f'{letras.lower()}', end = ' ')

print ()
print ('-'*60)

# Este programa analisa palavras