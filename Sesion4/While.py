#Para ejecutar cualquiera de los codigos, recuerde quitar el comentario al inicio de 
#la linea de código.

#----------------While-------------------
# x=0
# while x<10:
#     x+=1
#     print(x)

#-----------------Eco--------------------
# txt=''
# while txt!='salir':
#     txt=input('Ingrese una palabra: ')
#     print(txt)
# print('terminó')

#-----------Uso del break----------------
# x=0
# while x<10:
#     x+=1
#     if x==4:
#         break
#     print(x)

#-------------Uso del continue----------
# x=0
# while x<10:
#     x+=1
#     if x==4:
#         continue
#     print(x)

#-------------- Uso del pass -----------
# x=0
# while x<10:
#     pass

#------------- Bucle infinito------------
# txt=''
# while txt!='salir':
#     txt=input('Ingrese una palabra: ')
#     print(txt)

x=0       #Ojo el orden de las lineas de codigo SI IMPORTA "Ctrl+c" para terminar el programa
while x<10:
    print(x)
    if x==4:
        continue
    x+=1

