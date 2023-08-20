renda =float(input('qual o valor da sua renda?? '))
if renda > 2000:
    cal = renda * 2
    print('parabens, seu credito foi aprovado, o valor sera de \033[1:32m{:.2f}R$'.format(cal))
elif renda >= 1320:
    cal2 = renda / 4
    print('preciso te conhecer mais, seu credito sera de \033[1:33m{:.2f}R$.'.format(cal2))
  else:
      renda <= 1320
     print('poxa!!! infelizmente nao conseguimos credito para voce, tente na proxima vez.')
