soma = maiorvalor = contador = menorvalor = media = 0
resposta = 'S'

while resposta not in 'N':
    numero = int (input ('Digite um número: '))
    resposta = str (input ('Quer continuar? ')).upper().strip()[0]
    contador = contador + 1
    soma = soma + numero
    
    if contador == 1:
        maiorvalor = menorvalor = numero
    else:
        
        if maiorvalor < numero:
            maiorvalor = numero
        elif menorvalor > numero:
            menorvalor = numero
            
media = soma / contador
print (f'Você digitou {contador} números e a média entre eles é {media:.2f}')
print (f'O maior valor foi {maiorvalor} e o menor foi {menorvalor}')

# Este programa calcula analisa os números