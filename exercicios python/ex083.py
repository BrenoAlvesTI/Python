expr = str (input ('Digite a expressão: '))
pilha = list ()
for p in expr:
    if p == '(' or p == ')':
        pilha.append(p)
if pilha.count('(') == pilha.count(')'):
    print ('Sua expressão está válida!')
else:
    print ('Sua expressão está inválida!')

# Este programa indica se uma expressão é válida ou não de acordo com os parênteses