def voto(ano):
    from datetime import date
    a = date.today().year
    idade = a - n
    if idade < 16:
        return f"Com {idade} anos: NÂO VOTA"
    elif 16 <= idade < 18 or idade > 60:
        return f"Com {idade} anos: VOTO OPCIONAL"
    else:
        return f"Com {idade} anos: VOTO OBRIGATÓRIO"
    
n = int (input ('Ano de nascimento: '))
print (voto(n))

#Este programa verifica seu direito de voto