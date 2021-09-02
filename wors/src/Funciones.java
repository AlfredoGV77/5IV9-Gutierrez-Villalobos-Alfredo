
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.util.ArrayList;
import javax.swing.JOptionPane;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author bailarina77
 */
public class Funciones {
    
        private File archivo = new File("Frases.dat");
    private static ObjectInputStream entrada;
    private static ObjectOutputStream salida;
    ArrayList<Oraciones> listaOraciones = new ArrayList();


    public void agregarOracion(String oracion) throws IOException {

        Oraciones ora = new Oraciones(oracion);
        listaOraciones.add(ora);
        Guardar();
        JOptionPane.showMessageDialog(null, "La oracion a sido guardada");

    }

    public void Guardar() throws FileNotFoundException, IOException {

        ObjectOutputStream salida;
        FileOutputStream fo = new FileOutputStream(archivo);
        salida = new ObjectOutputStream(fo);
        salida.writeObject(listaOraciones);

        salida.close();

    }

    public ArrayList<Oraciones> Leer() throws FileNotFoundException, IOException, ClassNotFoundException {

        FileInputStream fi = new FileInputStream(archivo);
        ObjectInputStream entrada = new ObjectInputStream(fi);
        listaOraciones = (ArrayList)entrada.readObject();
        return listaOraciones;

    }
    
    
    
    
    
    
    
    
    
    
    
}
