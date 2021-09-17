from tkinter import *
from tkinter import messagebox as MessageBox

#NO BORREN ESTO, ES PA EL ERROR DE VARIABLES GLOBALES XDD
ventana_Inicio=None
cesar=None
trans=None
texto_cifrar=None
texto_cifrar2=None
texto_cifrado=None
desplazamiento=None

#defininimos la ventana de inicio

def ventana_inicio():
    global ventana_Inicio
    ventana_Inicio=Tk()
    #DEFINIMOS LAS PROPIEDAS DE LA VENTANA
    ventana_Inicio.geometry("300x250")
    ventana_Inicio.resizable(False,False)
    ventana_Inicio.config(bg="aqua")
    ventana_Inicio.title("BIENVENIDE USUARIE")
    Label(text="Escoja el tipo de cifrado", bg="snow", width="300", height="1", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Cifrado Cesar", height="3", width="30", bg="snow",command=cifradoCes).pack()
    Label(text="").pack()
    Button(text="Cifrado de Transposición", height="3", width="30", bg="snow", command=cifradoTrans).pack()
    Label(text="").pack()
    ventana_Inicio.mainloop()


#VENTANA PARA CIFRADO CESAR
def cifradoCes():
    global cesar
    cesar=Toplevel(ventana_Inicio)
    cesar.title("Cifrado y Descifrado Cesar")
    cesar.geometry("500x300")
    cesar.resizable(False,False)
    cesar.config(bg="aqua")
    global texto_cifrar, texto_cifrado,desplazamiento

    texto_cifrar=StringVar()
    desplazamiento=StringVar()
    
    
    Label(cesar,text="Holiiiiis xd", bg="aqua").pack()
    Label(cesar,text="").pack()
    
    Etiqueta_texto_cifrar=Label(cesar,text="Texto a cifrar/decifrar, ploz", bg="aqua")
    Etiqueta_texto_cifrar.pack()
    
    Entrada_texto_cifrar=Entry(cesar,textvariable=texto_cifrar)
    Entrada_texto_cifrar.pack()
    
    Etiqueta_desplazamiento=Label(cesar,text="Desplazamiento del cifrado ploz", bg="aqua")
    Etiqueta_desplazamiento.pack()
    Entrada_Desplazamiento=Entry(cesar,textvariable=desplazamiento)
    Entrada_Desplazamiento.pack()
    
    
    Button(cesar, text="Cifrar", width=10, height=1, bg="aqua", command=cifrar).pack()
    Button(cesar, text="Decifrar", width=10, height=1, bg="aqua", command=decifrar).pack()


    
#METODOS PARA CIFRAR Y DECIFRAR EN CESAR SIUUUUUUUUU    
def cifrar():
    c=texto_cifrar.get()
    n=int(desplazamiento.get())
    if texto_cifrar.get()=="" or desplazamiento.get()=="":
        MessageBox.showinfo("Error","Ingresa los datos correctamente")
    else:
        frase_cifrada = cifrado_cesar(alfabeto,n,c)
        MessageBox.showinfo("Texto cifrado","El texto cifrado es:"+frase_cifrada)

def decifrar():
    c=texto_cifrar.get()
    n=int(desplazamiento.get())
    if texto_cifrar.get()=="" or desplazamiento.get()=="":
        MessageBox.showinfo("Error","Ingresa los datos correctamente")
    else:
        frase_decifrada = decodificar(alfabeto,n,c)
        MessageBox.showinfo("Texto cifrado","El texto decifrado es:"+frase_decifrada)
        
    
import string
alfabeto = list(string.ascii_lowercase)


#LOS METODOS CHIDOS EN LOS QUE LLAMAREMOS ARRIBA XD
def cifrado_cesar(alfabeto,n,texto):
    texto_cifrado = ""
    for letra in texto:
        if letra in alfabeto:
            indice_actual = alfabeto.index(letra)
            indice_cesar = indice_actual + n
            if indice_cesar > 25:
                indice_cesar -= 25
            texto_cifrado += alfabeto[indice_cesar]
        else:
            texto_cifrado += letra
    return texto_cifrado


def decodificar(alfabeto,n,texto):
    texto_decodificado = ""
    for letra in texto:
        if letra in alfabeto:
            indice_cesar = alfabeto.index(letra)
            indice_original = indice_cesar - n
            if indice_original <0 :
                indice_original += 25
            texto_decodificado += alfabeto[indice_original]
        else:
            texto_decodificado += letra
    return texto_decodificado



#VENTANA DEL CIFRADO DE TRANSPOSICION     
def cifradoTrans():
    global trans, texto_cifrar2
    trans=Toplevel(ventana_Inicio)
    trans.title("Cifrado en Transposicion")
    trans.geometry("500x300")
    trans.resizable(False,False)
    trans.config(bg="aqua")
    texto_cifrar2=StringVar()
    
    Label(trans,text="Holiiiiis xd", bg="aqua").pack()
    Label(trans,text="").pack()
    
    Etiqueta_texto_cifrar=Label(trans,text="Texto a cifrar/decifrar, ploz", bg="aqua")
    Etiqueta_texto_cifrar.pack()
    
    Entrada_texto_cifrar2=Entry(trans,textvariable=texto_cifrar2)
    Entrada_texto_cifrar2.pack()
    
    
    Button(trans, text="Cifrar", width=10, height=1, bg="aqua", command=cifrarTrans).pack() 
    Button(trans, text="Decifrar", width=10, height=1, bg="aqua", command=decifrarTrans).pack()     
   
   
   
#METODOS PARA CIFRAR Y DESCIFRAR EN TRANSPOSICION SIUUUUUUUUU    
def cifrarTrans():
    cadena=texto_cifrar2.get()
    if texto_cifrar2.get()=="":
        MessageBox.showinfo("Error","Ingresa los datos correctamente")
    else:
        vocales = {
            'a': 3,
            'e': 5,
            'i': 2,
            'o': 4,
            'u': 1
        }

        cadena = cadena.replace('a', '3')
        cadena = cadena.replace('e', '5')
        cadena = cadena.replace('i', '2')
        cadena = cadena.replace('o', '4')
        cadena = cadena.replace('u', '1')

        count = 0
        cadena1 = ''

        for x in cadena:

            count += 1

            if(count % 2 == 0):
                try:
                    cadena1 += '$' + x.capitalize()
                except Exception:
                    cadena1 += x

            else:
                cadena1 += x
                
        MessageBox.showinfo("texto cifrado:","El texto cifrado es: "+cadena1)





def decifrarTrans():
    cadena=texto_cifrar2.get()
    if texto_cifrar2.get()=="" :
        MessageBox.showinfo("Error","Ingresa los datos correctamente")
    else:
        count = 0

        limp = "$"
        cadena1 = ''

        for x in range(len(limp)): 

            cadena = cadena.replace(limp[x], "")
        

        cadena = cadena.replace('3', 'a')
        cadena = cadena.replace('5', 'e')
        cadena = cadena.replace('2', 'i')
        cadena = cadena.replace('4', 'o')
        cadena = cadena.replace('1', 'u')

        for x in cadena:

            count += 1

            if(count % 2 == 0):
                try:
                    cadena1 += x.lower()
                except Exception:
                    cadena1 += x

            else:
                cadena1 += x

        MessageBox.showinfo("texto cifrado:","El texto cifrado es: "+cadena1)
   





ventana_inicio()