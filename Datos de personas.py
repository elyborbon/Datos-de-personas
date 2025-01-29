class humano (): 
    def __init__(self, edad, nombre, ocupacion):
        self.edad = edad
        self.nombre = nombre 
        self.ocupacion = ocupacion 

    def presentar(self):
            presentacion = ("Hola mi nombre es {} mi edad es {} y mi ocupacion es {}")
            print (presentacion.format(self.nombre, self.edad, self.ocupacion))

            #Metodo para cambiar la ocupacion 
    def contratar (self, puesto):
         self.puesto = puesto
         print("{} ha sido contratado como {}".format(self.nombre, self.puesto))
         self.ocupacion = puesto

humano1 = humano (21, "Maria,"," estudiante")

humano1.presentar()
humano1.contratar("obrero")
humano1.presentar()