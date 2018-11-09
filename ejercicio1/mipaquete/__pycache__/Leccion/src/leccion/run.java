/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package leccion;

import java.util.Scanner;

/**
 *
 * @author USUARIO
 */
public class run {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        //Creamos el constructor de Emplreado
        Empleado e = new Empleado ("Luis", "Benitez","1105558066" , 0);
        System.out.println(e); 
        Scanner leer = new Scanner(System.in);
        //EmpleadoPorHoras e1 =new EmpleadoPorHoras();
        //System.out.println("Ingresee su nombre\n");
        //String nombre=leer.next();
        EmpleadoFijo e2 =new EmpleadoFijo();
        e2.set_sueldo_fijo(300.2);
        e2.set_descuento_seguro(10);
        System.out.println("Ingrese comision");
        double comision=leer.nextDouble();
        e2.setcomision_fija(comision);
        e2.setNombre("Ana");
        e2.setApellido("Diaz");
        System.out.println(e2.toString());
    }
    
}
