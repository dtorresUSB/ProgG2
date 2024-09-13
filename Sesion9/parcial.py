import math

def dardos(x,y):
    r=math.sqrt(x**2+y**2)

    if r<=1:
        print('Suma 10 puntos')
    elif r<=5:
        print('Suma 5 puntos')
    elif r<=10:
        print('Suma 1 punto')
    else:
        print('No suma puntos')

def main():
    x=float(input('Ingrese la coordenada en x: '))
    y=float(input('Ingrese la coordenada en y: '))
    dardos(x,y)

def nit():
    coeficientes=[71, 67, 59, 53, 47, 43, 41, 37, 29, 23, 19, 17, 13, 7, 3]
    coeficientes.reverse()
    num=input('Ingrese el nit de la empresa: ')
    n_nit=[]
    for i in range(len(num),0,-1):
        n_nit.append(num[i-1])
    print(n_nit)

    sumatoria=0
    for i in range(len(n_nit)):
        sumatoria+=(int(n_nit[i])*coeficientes[i])

    mod=sumatoria%11
    
    if mod<=1:
        print(f'El codigo de verificación es: {mod}')
    else:
        print(f'El codigo de verificación es: {11-mod}')

if __name__=="__main__":
    opc=input('Ingrese una opcion: ')
    if opc=='1':
        main()
    elif opc=='2':
        nit()