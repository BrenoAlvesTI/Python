s = c = 0
while True:
    n = int (input ('Digite um número: ([999] para parar) '))
    if n == 999:
        break
    s = s + n
    c = c + 1
print (f'Você digitou {c} números e a soma entre eles é {s}')

# Este programa soma números