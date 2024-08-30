
def suma(num1,num2):
    resultado=num1+num2
    return resultado

def resta(num1,num2):
    resultado=num1-num2
    return resultado

def main():
    a=float(input('Ingrese un numero: '))
    b=float(input('Ingrese otro numero: '))
    print('1. Suma\n2. Resta\n3. Multiplicacion\n4. Division\n')
    ope=input('Ingrese una operacion: ').capitalize()

    if ope=='1' or ope=='Suma':
        c=suma(a,b)
        print(f'La suma de {a} y {b} es: {c}')
    elif ope=='2' or ope=='Resta':
        c=resta(a,b)
        print(f'La resta de {a} y {b} es: {c}')




        

main()