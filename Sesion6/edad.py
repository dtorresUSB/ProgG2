#import bisiesto
from bisiesto import fcn_bisiesto as fc

def main():
    print(__name__)
    year=int(input('Ingrese su edad: '))

    for i in range(2024-year,2025):
        opc=fc(i)
        if opc:
            print(f'{i}...si es bisiesto')
        else:
            print(f'{i}...no es bisiesto')

if __name__=="__main__":
    main()