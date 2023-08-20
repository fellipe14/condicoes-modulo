salario = float(input('qual o valor do salario? '))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('seu salario era R${:.2f}, entao sera R${:.2f} agora'.format(salario,novo))
 