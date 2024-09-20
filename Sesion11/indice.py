class IMC:
    def __init__(self):
        self.nombre=None
        self.altura=None
        self.peso=None
    
    def getNombre(self):
        return self.nombre
    
    def getAltura(self):
        return self.altura
    
    def getPeso(self):
        return self.peso
    
    def setNombre(self,nombre:str):
        self.nombre=nombre
    
    def setAltura(self,altura:int):
        self.altura=altura

    def setPeso(self,peso:float):
        self.peso=peso

    def indice(self):
        imc=self.peso/(self.altura/100)**2
        
        if imc<18.5:
            txt='Por debajo'
        elif imc<=24.9:
            txt='Saludable'
        elif imc<=29.9:
            txt='Sobrepeso'
        elif imc<=34.9:
            txt='Obesidad I'
        elif imc<=39.9:
            txt='Obesidad II'
        else:
            txt='Obesidad III'
        return f'su IMC es de {imc:.2f} => {txt}'
    
def main():
    paciente=IMC()
    nombre = input('Cual es su nombre: ')
    altura = int(input('Cual es su altura: '))
    peso = float(input('Cual es su peso:'))

    paciente.setNombre(nombre)
    paciente.setAltura(altura)
    paciente.setPeso(peso)
    print(paciente.indice())

if __name__=="__main__":
    main()