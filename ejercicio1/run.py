from mipaquete.modelo import *
e=Empleado ()
e.agregar_nombre("Luis")
e.agregar_apellido("Benitez")
e.agregar_cedula("1100023924")
print(e.presentar_datos())

e1= Empleado_Por_Horas()
nombre = input("Ingrese su nombre\n")
e1.agregar_nombre(nombre)
e1.agregar_apellido("Andrade")
e1.cedula="1103424651"
e1.agregar_valor_hora(20.2)
e1.agregar_numero_horas(15)
print(e1.presentar_datos())

e2=Empleado_Fijo()
e2.agregar_sueldo(300.2)
e2.descuento_seguro= 10
comision = imput("Ingrese comision:\n")
comision= float(comision)
e2.agregar_comision_fija(comision)
e2.nombre ="Ana"
e2.apellido="Díaz"
print(e2.presentar_datos())