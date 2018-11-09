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
public class EmpleadoPorSemanas extends Empleado {

    private double numero_semanas;
    private double valor_semanal;

    public EmpleadoPorSemanas(String n, String a, String c, double cf, double ns, double vs) {
        //Heredamos 
        super(n, a, c, cf);
        //Agregamos los set y get que nos faltan
        setNumero_semanas(ns);
        setValor_semanal(vs);
    }

    //Agregar
    public void setNumero_semanas(double ns) {
        numero_semanas = ns;
    }

    public void setValor_semanal(double vs) {
        valor_semanal = vs;
    }

    public double getNumero_semanas() {
        return numero_semanas;
    }

    public double getValor_semanal() {
        return valor_semanal;
    }

    public double calcular_sueldo_final() {
        double calculo = (getValor_semanal() * getNumero_semanas()) + getComisionFija());
        return calculo;
    }

}
