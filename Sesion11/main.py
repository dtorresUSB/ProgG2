class Materias:
    def __init__(self):
        self.__nombre=None
        self.creditos=None
        self.profesor=None
        self.horario=None
        self.salon=None
        
    def metHorario(self):
        return (f"La materia {self.nombre} tiene {self.creditos} "
                f"creditos, esta a cargo del profesor {self.profesor} "
                f"en el horario de {self.horario} "
                f"en el salon {self.salon}.")

def main():
    materias=[]
    asignaturas=[["Programacion Aplicada a Sistemas Mecatronicos",
                  "2","David Torres","Miercoles - Viernes 9 a 11 am",
                  "GO 203"],
                 ["Calculo Integral","3","Patricia Aragon",
                  "Martes - Jueves 7 a 9 am","DB 403"],
                 ["Materiales","2","Elmer Cepeda","Martes - Jueves 9 a 11 am",
                  "DS 517"]]

    for i in range(3):
        val=Materias()
        materias.append(val)
        materias[i].nombre=asignaturas[i][0]
        materias[i].creditos=asignaturas[i][1]
        materias[i].profesor=asignaturas[i][2]
        materias[i].horario=asignaturas[i][3]
        materias[i].salon=asignaturas[i][4]



    materia4=Materias()
    materia4.nombre="Fisica Mecanica"
    materia4.creditos="3"
    materia4.profesor="Jorge Caicedo"
    materia4.horario="Miercoles - Viernes 11 a 1 pm"
    materia4.salon="DB 403"
    materias.append(materia4)

    materia5=Materias()
    materia5.nombre="Historia Politica y Formacion"
    materia5.creditos="2"
    materia5.profesor="Alexandra Arias"
    materia5.horario=" Martes 11 a 1 pm"
    materia5.salon="PS 103"
    materias.append(materia5)

    materia6=Materias()
    materia6.nombre="Algebra Lineal"
    materia6.creditos="3"
    materia6.profesor="Olga Garatejo"
    materia6.horario="Miercoles - Viernes 7 a 9 am"
    materia6.salon="PS 202"
    materias.append(materia6)

    materia7=Materias()
    materia7.nombre="Dibujo de Ingenieria"
    materia7.creditos="2"
    materia7.profesor="Elmer Cepeda"
    materia7.horario="Viernes 1 a 3 pm"
    materia7.salon="DS 104"
    materias.append(materia7)

    print('Escoja una de las siguientes opciones: \n'
          '1. Programacion\n'
          '2. Calculo\n'
          '3. Materiales\n'
          '4. Fisica Mecanica\n'
          '5. Historia Politica\n'
          '6. Algebra\n'
          '7. Dibujo\n')
    elegir=int(input("Ingrese la materia que desea consultar:"))

    if 0<elegir<7:
        print(materias[elegir-1].metHorario())
    else:
        print("Esta materia no se encuentra")
    
if __name__=="__main__":
    main()


    





