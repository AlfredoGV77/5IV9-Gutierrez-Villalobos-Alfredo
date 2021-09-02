/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package calculadora.cientifica;

import java.util.ArrayList;

/**
 *
 * @author bailarina77
 */
public class Operaciones {
    
    private ArrayList<Operacion> historial= new ArrayList<>();

    public Operaciones() {}
    
    public ArrayList<Operacion> getHistorial(){
        return historial;
    }
    
    public void setHistorial(ArrayList<Operacion>historial){
        this.historial=historial;
    }
    
    public void agregarHistorial(Operacion operacion){
        for(Operacion ops:historial){
            historial.add(operacion);
        }
    }
    
    public void listarHistorial(){
    for(Operacion lista:historial){
         System.out.println(lista.getOperacionfinal()+"="+lista.getResultadofinal());
    }
}
    
    
}
