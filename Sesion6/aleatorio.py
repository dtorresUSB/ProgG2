from random import randint as r

secret=r(0,10)
while 1:
    num=int(input('Cual es el numero: '))
    if num==secret:
        print(f'Felicitaciones, el numero es {secret}')
        break
    else:
        print('JA JA ese no es el numero....')
