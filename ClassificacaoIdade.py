idade = int(input('informe a sua idade: '))
if idade <= 12:
    print('Classificação: Criança')
elif idade > 12 and idade <= 18:
    print('Classificação: Adolescente')
else:
    print('Classificação: Adulto')