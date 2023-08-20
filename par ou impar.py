numero = int(input('me diga um numero: '))
resultado = numero % 2
if resultado == 0:
    print('o numero {} e par'.format(numero))
else:
    print('o numero {} e impar'.format(numero))