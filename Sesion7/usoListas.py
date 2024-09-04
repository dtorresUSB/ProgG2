def agregar(lista):
    num=int(input('Que número desea usted agregar: '))
    lista.append(num)
    return lista

def insertar(lista):
    idx=int(input('Indique el indice del elemento a insertar: '))
    num=int(input('Cual es el número que desea insertar: '))
    lista.insert(idx,num)
    return lista

def borrar(lista):
    lista.clear()
    return lista

def main():
    lista=[2,54,15]

    while 1:
        print('\nMenú de uso de listas: \n'
          '1. Agregar un elemento a la lista.\n'
          '2. Insertar un elemento dentro de la lista\n'
          '3. Borrar por completo la lista\n')
        opc=input('Seleccione una de las opciones: ')

        if opc=='1':
            lista=agregar(lista)
        elif opc=='2':
            lista=insertar(lista)
        elif opc=='3':
            lista=borrar(lista)
        print(lista)

        if opc=='salir':
            break

if __name__=="__main__":
    main()