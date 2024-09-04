from factorial import fcn_factorial as fac

def main():
    n=int(input('Ingrese el numero de equipos: '))
    m=int(input('Ingrese el numero de grupos: '))
    binomial=(fac(n))/(fac(m)*fac(n-m))
    print(f'El numero de combinaciones es: {binomial}')

main() 