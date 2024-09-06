#Programa de matrices hecho con la opcion 2 de la clase
from random import randint as r

def matriz(filas,columnas):
    matrix=[]
    for i in range(filas):
        matrix.append([])
        for j in range(columnas):
            #num=int(input(f'Ingrese un valor en la posición [{i}][{j}]: '))
            num=r(-20,20)
            matrix[i].append(num)
    #print(matrix)
    return matrix

def impresion(x):
    for i in x:
        print(i)

def producto(matriz):
    nueva=[]
    escalar=int(input('Ingrese el valor a escalar la matriz: '))
    for i in range(len(matriz)):
        fila=[]
        for j in range(len(matriz[0])):
            num=escalar*matriz[i][j]
            fila.append(num)
        nueva.append(fila)
    #print(matrix)
    return nueva

def main():
    filas = int(input('Ingrese el numero de filas: '))
    columnas = int(input('Ingrese el numero de columnas: '))
    x=matriz(filas,columnas)
    impresion(x)
    y=producto(x)
    impresion(y)

if __name__=="__main__":
    main()
