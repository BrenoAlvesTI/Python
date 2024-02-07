lista = list ()
for c in range (1,6):
    n = int (input('Digite um valor: '))
    if c == 1 or n > lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos = pos + 1
print ('=-='*20)
print (f'Os valores digitados em ordem foram: {lista}')
print ('=-='*20)

# Este programa informa os números em ordem crescente sem usar a função sort()