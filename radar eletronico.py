velocidade = float(input('qual a velocidade do carro? '))
if velocidade >80:
    print('MULTADO  voce excedeu o limite de velocidade que e 80 Km/h')
    #calculo de multa com a velocidade excedente
    multa = (velocidade-80) * 7
    print('voce recebeu uma multa de R$ {:.2f}:'.format(multa))
print('tenha um bom dia')