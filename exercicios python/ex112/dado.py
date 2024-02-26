def leiaD(msg):
    ok = False
    while not ok:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print (f'ERRO! "{entrada}" não é um preço válido.')
        else:
            ok = True
            return float(entrada)