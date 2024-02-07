matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = maiorvalor = somacoluna3 = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite o valor para a posicão {l}, {c}: '))
print ('=-='*20)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}] ', end ='')
        if matriz[l][c] % 2 == 0:
            somapar = somapar + matriz[l][c]
    print()
print ('=-='*20)
print (f'A soma dos pares é {somapar}.')
for l in range (0,3):
    somacoluna3 = somacoluna3 + matriz[l][2]
print (f'A soma da terceira coluna é {somacoluna3}.')
for c in range(0,3):
    if c == 0:
        maiorvalor = matriz[1][c]
    elif matriz[1][c] > maiorvalor:
        maiorvalor = matriz[1][c]
print (f'O maior valor da segunda coluna é {maiorvalor}.')

# Este programa analisa a matriz