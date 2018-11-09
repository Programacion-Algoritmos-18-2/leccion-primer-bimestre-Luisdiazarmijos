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
public class Empleado {

    //Definimos atributos
    private String nombre;
    private String apellido;
    private String cedula;
    private double comision_fija;
    //Construimos los agregar y presentar 

    public Empleado(String n, String a, String c, double cf) {

        setNombre(n);
        setApellido(a);
        setcedula(c);
        setcomision_fija(cf);
    }

    public void setNombre(String n) {
        nombre = n;
    }

    public void setApellido(String n) {
        apellido = n;
    }

    public void setcedula(String n) {
        cedula = n;
    }

    public void setcomision_fija(double n) {
        comision_fija = n;
    }

    public String getNombre() {
        return nombre;
    }

    public String getApellido() {
        return apellido;
    }

    public String getCedula() {
        return cedula;
    }

    public double getComisionFija() {
        return comision_fija;
    }
    @Override
    public String toString(){
        return String.format("Nombre: %s \n Apellido: %s \n Cedula: %s \n Comision Fija: %.2f", 
                getNombre(), getApellido(), getCedula(), getComisionFija());
    }
    
    
}

