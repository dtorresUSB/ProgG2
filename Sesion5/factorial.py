def factorial(n):
    a=1
    for i in range(1,n+1):
        a*=i
    return a

def main():
    n=int(input('Ingrese el numero de equipos: '))
    m=int(input('Ingrese el numero de grupos: '))
    binomial=(factorial(n))/(factorial(m)*factorial(n-m))
    print(f'El numero de combinaciones es: {binomial}')

main()  
