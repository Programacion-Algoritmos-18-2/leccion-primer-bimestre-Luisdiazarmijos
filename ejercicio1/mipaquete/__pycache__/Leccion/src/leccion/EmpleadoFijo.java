/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package leccion;

/**
 *
 * @author USUARIO
 */
//Heredamos la clase Empleado
public class EmpleadoFijo extends Empleado {

    //Declaramos las variables que nso faltan
    private double sueldo_fijo;
    private double descuento_seguro;
    public EmpleadoFijo(){}
    public EmpleadoFijo(String n, String a, String c, double cf, double sf, double ds) {
        //Heredamos 
        super(n, a, c, cf);
        //Agregamos los set y get que nos faltan
        set_sueldo_fijo(sf);
        set_descuento_seguro(ds);
    }

    public void set_sueldo_fijo(double sf) {
        sueldo_fijo = sf;
    }

    public void set_descuento_seguro(double ds) {
        descuento_seguro = ds;
    }

    public double get_sueldo_fijo() {
        return sueldo_fijo;
    }
    public double get_descuento_seguro(){
        return descuento_seguro;
    }
    public double calcular_sueldo_final(){
       double sueldo_final =(get_sueldo_fijo()+ getComisionFija() - get_descuento_seguro()/100);
                
        return sueldo_final;
    }

}
