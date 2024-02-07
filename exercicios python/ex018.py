from math import radians,sin,cos,tan
a = float (input ('Digite o ângulo: '))
s = sin (radians(a))
c = cos (radians(a))
t = tan (radians(a))
print (f'O Seno de {a} é: {s:.2f}')
print (f'O cosceno de {a} é: {c:.2f}')
print (f'A tangente de {a} é: {t:.2f}')

# Este programa diz Seno, cosceno e tangente de um ângulo