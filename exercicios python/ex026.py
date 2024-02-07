f = str (input ('Digite uma frase: ')).upper().strip()
qa = f.count('A')
pa = (f.find('A')+1)
ua = (f.rfind('A')+1)
print (f'A frase tem {qa} letra A, o primeiro A aparece na posição {pa} e o último A aparece na posição {ua}.')

# Este programa analisa a letra "A" em uma frase
