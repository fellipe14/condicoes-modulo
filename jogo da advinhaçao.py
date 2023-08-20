from random import randint
#faz o computador pensar
computador = randint(0,5)
print('-=-' * 20)
print('vou pensar em um numero de 0 a 5, tente advinhar...')
print('-=-' * 20)
#jogador tenta advinhar
jogador = int(input('em que numero pensei? '))
if jogador == computador:
    print('carai boracha, acertou kkk')
else:
    print('EROOOUUU, KKKK VENCI OTARIO')