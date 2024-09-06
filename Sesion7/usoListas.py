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

def remover(lista):
    num=int(input('Que numero desea remover: '))
    lista.remove(num)
    return lista

def indice(lista):
    num=int(input('Que numero busca: '))
    pos=lista.index(num)
    print(f'El número {num} se encuentra en la posicion {pos}')
    return lista

def minimo(lista):
    valor=min(lista)
    print(f'El valor minimo es {valor}')
    return lista

def main():
    lista=[2,54,15]

    while 1:
        print('\nMenú de uso de listas: \n'
          '1. Agregar un elemento a la lista.\n'
          '2. Insertar un elemento dentro de la lista\n'
          '3. Borrar por completo la lista\n'
          '4. Remover un elemento de la lista\n'
          '5. Busqueda del indice de un número\n'
          '6. Encontrar el valor minimo de una lista')
        opc=int(input('Seleccione una de las opciones: '))

        menu=[agregar,insertar,borrar,remover,
              indice, minimo]
        lista=menu[opc-1](lista)
        print(lista)

        if opc=='salir':
            break

if __name__=="__main__":
    main()