/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package calculadora.cientifica;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.util.ArrayList;
import javax.swing.JOptionPane;

/**
 *
 * @author bailarina77
 */
public class Funciones {
    private File archivo=new File("Operaciones.dat");
    private static ObjectInputStream entrada;
    private static ObjectOutputStream salida;
    public  ArrayList<Operacion> listaOperaciones=new ArrayList();
    
    
    
    //CREAMOS LOS METODOS
    
    public void agregarOperaciones(String operacionfinal, double resultadofinal ) throws IOException{
        Operacion o=new Operacion(operacionfinal, resultadofinal);
        ///listaOperaciones.add(o);
        listaOperaciones.add(o);
        Guardar();
    }
    
    public void Guardar() throws FileNotFoundException, IOException{
        ObjectOutputStream salida;
        FileOutputStream fo = new FileOutputStream(archivo);
        salida = new ObjectOutputStream(fo);
        salida.writeObject(listaOperaciones);
        salida.close();
    }
    
    
    public ArrayList<Operacion> Leer() throws FileNotFoundException, IOException, ClassNotFoundException{
        
        FileInputStream fi = new FileInputStream(archivo);
        ObjectInputStream entrada = new ObjectInputStream(fi);
        listaOperaciones = (ArrayList)entrada.readObject();
        return listaOperaciones;
    }


    public void listarHistorial() throws FileNotFoundException, IOException, ClassNotFoundException{
        FileInputStream fi = new FileInputStream(archivo);
        ObjectInputStream entrada = new ObjectInputStream(fi);
        listaOperaciones = (ArrayList)entrada.readObject();
    for(Operacion lista:listaOperaciones){
         System.out.println(lista.getOperacionfinal()+" holaaaaaaaaaaaaaaaaaaaa ="+lista.getResultadofinal());
    }
}    
    
    
    
}
