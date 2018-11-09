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
    def obtener_comision_fija(self):
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
class Empleado_Por_Horas(Empleado):
  
    def __init__(self):
        super(Empleado_Por_Horas, self).__init__()
        self.numero_horas=0
        self.valor_hora=0

        #Declaramos los agregar y obteter respectivamente
    def agregar_numero_horas(self, n):  
        self.numero_horas = n

    def obtener_numero_horas(self):
        return self.numero_horas
    def agregar_valor_hora(self, n):  
        self.valor_hora = n

    def obtener_valor_hora(self):
        return self.valor_hora
        #Metodo para calcular el sueldo final
    def calcular_valor_sueldo(self):
        return(self.numero_horas * self.valor_hora)+ self.comision_fija
        

    def presentar_datos(self):
        cadena="%s\n Número horas:%s\n Valor hora: %s\n Sueldo final: %s"%(super(Empleado_Por_Horas,self).presentar_datos(),
                                                                           self.obtener_numero_horas(),self.obtener_valor_hora(),self.calcular_valor_sueldo())
        return cadena
    

# Hacemos la clase y heredamos de la clase Empleado
class Empleado_Fijo(Empleado):
   
     def __init__(self):
        super(Empleado_Fijo,Empleado.__init__()
        self.sueldo_fijo = 0
        self.descuento_seguro = 0
#Declaramos los agregar y obteter respectivamente

    def agregar_sueldo_fijo(self, n):
       self.sueldo_fijo =n   
    def obtener_sueldo_fijo(self):
        sueldo_fijo =

    def agregar_descuento_seguro(self, n):
        self.descuento_fijo =n
    def obtener_descuento_seguro(self):
        return self.descuento_seguro
    def agregar_sueldo_final(self, n):
        self.sueldo_final = n
    def obtener_sueldo_final(self):
        return self.sueldo_final
    def calcular_sueldo_final(self):
        sueldo_final =(self.obtener_sueldo_fijo()+self.obtener_comision_fija()-self.obtener_descuento_seguro()/100)
        return sueldo_final
    def presentar_datos(self):
        cadena="%s\n sueldo_fijo:%s\n descuento_seguro:%s\n sueldo_final:%s"%(super(Empleado_Fijo, self).presentar_datos(),self.obtener_sueldo_fijo(),self.obtener_sueldo_final(),self.calcular_sueldo_final())
        return cadena
# Hacemos la clase y heredamos de la clase Padre
class Empleado_Por_Semana(object):
    def __init__(self, arg):
        super(Emplead_Por_Semana, self).__init__()
        self.numero_semanas=0
        self.valor_semanal=0
#Agregamos los agregar y obtener respectivamente 
    def agregar_numero_semanas(self, n):
        self.numero_semanas = n
    def obtener_numero_semanas(self):
        return self.numero_semanas
    def agregar_valor_semanal(self, n):
        self.valor_semanal =n
    def obtener_valor_semanal(self):
        return self.valor_semnal

  #Metodo de calcular valor final
  def calcular_sueldo_final(self):
      return(self.numero_semanas* self.valor_semanal) * self.comision_fija
  #Metodo de presentar datos
  def presentar_datos(self):
      cadena ="%s\n numero_semanas: %s\n valor_semanal: %s\nsueldo_final: %s"%(super(Empleado_Por_Semana,self).presentar_datos()),
                                                                                self.obtener_numero_semanas(),self.obtener_valor_semanal();self.calcular_valor_sueldo())
      return cadena