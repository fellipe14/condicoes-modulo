distancia = float(input('qual e a distancia da sua viagem?  '))
print( 'voce esta preste a começar uma viagem de {}km'.format(distancia))
if distancia <=200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('seu gasto na viagem sera {:.2f}'.format(preco))