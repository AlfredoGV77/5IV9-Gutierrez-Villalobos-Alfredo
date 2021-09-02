/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package calculadora.cientifica;
import java.io.Serializable;
/**
 *
 * @author bailarina77
 */
public class Operacion implements Serializable{
    private String operacionfinal;
    private double resultadofinal;
    

    public Operacion(String operacionfinal, double resultadofinal) {
        this.operacionfinal = operacionfinal;
        this.resultadofinal = resultadofinal;
    }

    public String getOperacionfinal() {
        return operacionfinal;
    }

    public void setOperacionfinal(String operacionfinal) {
        this.operacionfinal = operacionfinal;
    }

    public double getResultadofinal() {
        return resultadofinal;
    }

    public void setResultadofinal(double resultadofinal) {
        this.resultadofinal = resultadofinal;
    }
    
    
    
    
}
