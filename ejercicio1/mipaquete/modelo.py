#Definimos la clase
class Empleado (object):
      #Definimos atributos
    def __init__(self):
    
        self.nombre =" "
        self.apellido=" "
        self.cedula=" "
        self.comision_fija= 0
    #Construimos los agregar y presentar 
    def agregar_comision_fija(self,comision):
        
        self.comision_fija=comision
        pass
    def obtener_comision(self):
        return self.comision_fija
        pass
    
    def agregar_nombre(self, n):  
        self.nombre = n

    def obtener_nombre(self):
        return self.nombre

    def agregar_apellido(self, a):  
        self.apellido = a

    def obtener_apellido(self):
        return self.apellido

    def agregar_cedula(self, c):
        self.cedula = c
        pass
    def obtener_cedula(self):
        return self.cedula
        pass
    def presentar_datos(self):
        return "Informacion de:%s-%s\n\tCedula:-%s" % (self.obtener_nombre(), self.apellido, self.obtener_cedula())
# Hacemos la clase y heredamos de la clase materia

        

