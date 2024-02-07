c = 0
s = 0
n = int (input ('Digite um número: Digite [999] para parar '))
while n != 999:
    s = s + n
    c = c + 1
    n = int (input ('Digite um número: Digite [999] para parar '))
print (f'Você digitou {c} números e a soma entre eles é {s}')

# Este programa soma números