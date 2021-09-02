
import java.io.Serializable;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author bailarina77
 */
import java.io.Serializable;
public class Oraciones implements Serializable{

    public Oraciones(String oracion) {
        this.oracion = oracion;
    }
    private String oracion;

    public String getOracion() {
        return oracion;
    }

    public void setOracion(String oracion) {
        this.oracion = oracion;
    }
}

