from tkinter import *
import os
from datetime import datetime
from tkinter import ttk
import tkinter.filedialog
import tkinter as tk
import xml.etree.ElementTree as ET

from Circular import ListaCircular
from ORTOGONAL import lista_Ortogonal
DATOS= ListaCircular()
REPORTE=ListaCircular()
def CREAR_INTERFAZ():
    def OP1():
        def  LOAD():
            name=desplegable.get()
            print("HOLA SOY LA ORIGINAL")
            DATOS.buscar(name)
            imagen=PhotoImage(file="matrix.png")
            Label(op1,image=imagen).place(x=20,y=100).pack()
        def ROTAR_IMG():    
            name=desplegable.get()
            print("HOLA TOY ROTANDO")
            DATOS.buscar_y_rotar_horizontal(name)
            
            imagen2=PhotoImage(file="matrix_horizontal.png")
            Label(op1,image=imagen2).place(x=500,y=100).pack()
        L1=StringVar()
        widget=StringVar()  
        op1=Toplevel()

        op1.title("ROTACION HORIZONTAL")
        op1.iconbitmap('icono.ico')
        op1.geometry("1200x700")
        op1.config(bg="#0044A3")
        Label(op1,textvariable=L1,font="Helvetica 16",bg="#0044A3").place(x=30,y=20)
        L1.set("Seleccione una matriz")
        Label(op1,textvariable=widget,font="Helvetica 16",bg="#0044A3").place(x=30,y=70)
        #frame.config(bg="#0044A3",width="400", height="400")
        desplegable=ttk.Combobox(op1,width=20,font="Helvetica 14",state="readonly")
        desplegable.place(x=250,y=20)
        desplegable['values']=DATOS.NOMBRES()

        Button(op1,text="ROTAR",command=ROTAR_IMG,font="Helvetica 12",bg="gold").place(x=650, y=20)
        Button(op1,text="CARGAR IMAGEN",command=LOAD,font="Helvetica 12",bg="gold").place(x=500, y=20)
        op1.mainloop()

    def OP2():
        def  LOAD():
            name=desplegable.get()
            print("HOLA SOY LA ORIGINAL")
            DATOS.buscar(name)
            imagen=PhotoImage(file="matrix.png")
            Label(op2,image=imagen).place(x=20,y=100).pack()
        def ROTAR_IMG():    
            name=desplegable.get()
            print("HOLA TOY ROTANDO")
            DATOS.buscar_y_rotar_vertical(name)
            
            imagen2=PhotoImage(file="matrix_vertical.png")
            Label(op2,image=imagen2).place(x=500,y=100).pack()
        L2=StringVar()
        op2=Toplevel()
        op2.title("ROTACION VERTICAL")
        op2.iconbitmap('icono.ico')
        op2.geometry("1200x700")
        op2.config(bg="#0044A3")
        Label(op2,textvariable=L2,font="Helvetica 16",bg="#0044A3").place(x=30,y=20)
        L2.set("Seleccione una matriz")
        #frame.config(bg="#0044A3",width="400", height="400")
        desplegable=ttk.Combobox(op2,width=20,font="Helvetica 14")
        desplegable.place(x=250,y=20)
        desplegable['values']=DATOS.NOMBRES()

        Button(op2,text="ROTAR",command=ROTAR_IMG,font="Helvetica 12",bg="gold").place(x=650, y=20)
        Button(op2,text="CARGAR IMAGEN",command=LOAD,font="Helvetica 12",bg="gold").place(x=500, y=20)
        op2.mainloop()
    
    def OP3():
        def  LOAD():
            name=desplegable.get()
            print("HOLA SOY LA ORIGINAL")
            DATOS.buscar(name)
            imagen=PhotoImage(file="matrix.png")
            Label(op3,image=imagen).place(x=20,y=100).pack()
        def ROTAR_IMG():    
            name=desplegable.get()
            print("HOLA TOY ROTANDO")
            DATOS.buscar_transpuesta(name)
            
            imagen2=PhotoImage(file="matrix_transpuesta.png")
            Label(op3,image=imagen2).place(x=500,y=100).pack()
        L1=StringVar()
        widget=StringVar()  
        op3=Toplevel()

        op3.title("TRANSPUESTA")
        op3.iconbitmap('icono.ico')
        op3.geometry("1200x700")
        op3.config(bg="#0044A3")
        Label(op3,textvariable=L1,font="Helvetica 16",bg="#0044A3").place(x=30,y=20)
        L1.set("Seleccione una matriz")
        Label(op3,textvariable=widget,font="Helvetica 16",bg="#0044A3").place(x=30,y=70)
        #frame.config(bg="#0044A3",width="400", height="400")
        desplegable=ttk.Combobox(op3,width=20,font="Helvetica 14",state="readonly")
        desplegable.place(x=250,y=20)
        desplegable['values']=DATOS.NOMBRES()

        Button(op3,text="ROTAR",command=ROTAR_IMG,font="Helvetica 12",bg="gold").place(x=650, y=20)
        Button(op3,text="CARGAR IMAGEN",command=LOAD,font="Helvetica 12",bg="gold").place(x=500, y=20)
        op3.mainloop()

    def OP4():
        def  LOAD():
            #obteniendo valores
            name=desplegable.get()
            Po=xo.get()
            Qo=yo.get()
            P=x.get()
            Q=y.get()
            
            
            
        def ROTAR_IMG():    
            name=desplegable.get()
            print("HOLA TOY ROTANDO")
            DATOS.buscar_transpuesta(name)
            
            imagen2=PhotoImage(file="matrix_transpuesta.png")
            Label(op4,image=imagen2).place(x=500,y=100).pack()
        L1=StringVar()

        l2=StringVar()
        l3=StringVar()
        l4=StringVar()
        l5=StringVar()
  
        op4=Toplevel()
        """miframe=Frame(op4,width=1000,height=1000)
        miframe.config(bg="#0044A3")
        miframe.pack(fill="both",expand="True")
        mimagen=PhotoImage(file="matrix.png")
        Label(miframe,image=mimagen).place(x=10,y=10)
        mimagen2=PhotoImage(file="matrix_transpuesta.png")
        Label(miframe,image=mimagen2).place(x=400,y=10)"""
        xo=IntVar()
        yo=IntVar()
        x=IntVar()
        y=IntVar()
        
        op4.title("LIMPIAR ZONA")
        op4.iconbitmap('icono.ico')
        op4.geometry("1200x700")
        op4.config(bg="#0044A3")

        Label(op4,textvariable=L1,font="Helvetica 16",bg="#0044A3").place(x=30,y=20)
        L1.set("Seleccione una matriz")

        Label(op4,textvariable=l2,font="Helvetica 12",bg="#0044A3").place(x=30,y=100)
        l2.set("Xo")
        Label(op4,textvariable=l3,font="Helvetica 12",bg="#0044A3").place(x=30,y=140)
        l3.set("Yo")
        Label(op4,textvariable=l4,font="Helvetica 12",bg="#0044A3").place(x=250,y=100)
        l4.set("X")
        Label(op4,textvariable=l5,font="Helvetica 12",bg="#0044A3").place(x=250,y=140)
        l5.set("y")

        #frame.config(bg="#0044A3",width="400", height="400")
        desplegable=ttk.Combobox(op4,width=20,font="Helvetica 14",state="readonly")
        desplegable.place(x=250,y=20)
        desplegable['values']=DATOS.NOMBRES()
        
        Entry(op4,textvariable=xo,font="Helvetica 12").place(x=60,y=100)
        Entry(op4,textvariable=yo,font="Helvetica 12").place(x=60,y=140)
        Entry(op4,textvariable=x,font="Helvetica 12").place(x=270,y=100)
        Entry(op4,textvariable=y,font="Helvetica 12").place(x=270,y=140)

        Button(op4,text="LIMPIAR",command=ROTAR_IMG,font="Helvetica 12",bg="gold").place(x=650, y=20)
        Button(op4,text="CARGAR IMAGEN",command=LOAD,font="Helvetica 12",bg="gold").place(x=500, y=20)
        op4.mainloop()
    
    def OP5():
        def  ROTH():
            print("HOLA TOY ROTANDO")
        L1=StringVar()
        op1=Toplevel()
        op1.title("AGREGAR LINEA HORIZONTAL")
        op1.iconbitmap('icono.ico')
        op1.geometry("800x500")
        op1.config(bg="#0044A3")
        Label(op1,textvariable=L1,font="Helvetica 16",bg="#0044A3").place(x=30,y=20)
        L1.set("Seleccione una matriz")
        #frame.config(bg="#0044A3",width="400", height="400")
        desplegable=ttk.Combobox(op1,width=20,font="Helvetica 14")
        desplegable.place(x=250,y=20)
        desplegable['values']=DATOS.NOMBRES()

        Button(op1,text="ROTAR",command=ROTH,font="Helvetica 12",bg="gold").place(x=500, y=20)
        
        op1.mainloop()

    def OP6():
        def  ROTV():
            print("HOLA TOY ROTANDO")
        L2=StringVar()
        op2=Toplevel()
        op2.title("AGREGAR LINEA VERTICAL")
        op2.iconbitmap('icono.ico')
        op2.geometry("800x500")
        op2.config(bg="#0044A3")
        Label(op2,textvariable=L2,font="Helvetica 16",bg="#0044A3").place(x=30,y=20)
        L2.set("Seleccione una matriz")
        #frame.config(bg="#0044A3",width="400", height="400")
        desplegable=ttk.Combobox(op2,width=20,font="Helvetica 14")
        desplegable.place(x=250,y=20)
        desplegable['values']=DATOS.NOMBRES()

        Button(op2,text="ROTAR",command=ROTV,font="Helvetica 12",bg="gold").place(x=500, y=20)
        
        op2.mainloop()
    
    def OP7():
        def  ROTH():
            print("HOLA TOY ROTANDO")
        L1=StringVar()
        op1=Toplevel()
        op1.title("AGREGAR RECTANGULO")
        op1.iconbitmap('icono.ico')
        op1.geometry("800x500")
        op1.config(bg="#0044A3")
        Label(op1,textvariable=L1,font="Helvetica 16",bg="#0044A3").place(x=30,y=20)
        L1.set("Seleccione una matriz")
        #frame.config(bg="#0044A3",width="400", height="400")
        desplegable=ttk.Combobox(op1,width=20,font="Helvetica 14")
        desplegable.place(x=250,y=20)
        desplegable['values']=DATOS.NOMBRES()

        Button(op1,text="ROTAR",command=ROTH,font="Helvetica 12",bg="gold").place(x=500, y=20)
        
        op1.mainloop()

    def OP8():
        def  ROTV():
            print("HOLA TOY ROTANDO")
        L2=StringVar()
        op2=Toplevel()
        op2.title("AGREGAR TRIANGULO RECTANGULO")
        op2.iconbitmap('icono.ico')
        op2.geometry("800x500")
        op2.config(bg="#0044A3")
        Label(op2,textvariable=L2,font="Helvetica 16",bg="#0044A3").place(x=30,y=20)
        L2.set("Seleccione una matriz")
        #frame.config(bg="#0044A3",width="400", height="400")
        desplegable=ttk.Combobox(op2,width=20,font="Helvetica 14")
        desplegable.place(x=250,y=20)
        desplegable['values']=DATOS.NOMBRES()

        Button(op2,text="ROTAR",command=ROTV,font="Helvetica 12",bg="gold").place(x=500, y=20)
        
        op2.mainloop()


    def DIALOGO():
        global DATOS,REPORTE
        fd= tkinter.Tk()
        fd.withdraw()
        ruta=tkinter.filedialog.askopenfilename(
            initialdir="C:", 
            filetypes=(
                ("Fichero XML ", "*.xml"),
                ("Todos los ficheros","*.*")
            ), 
            title = "ABRIR ARCHIVO"
        )
        try:
            print("------> "+ ruta)
            rut.set("CARGA EXITOSA")
            print("")
            print("")
            #lectura de archivo XML
            tree=ET.parse(ruta)
            a=tree.getroot()
            #print("--------Todos los atributos--------")
            for elemento in a:
                
                for subelemento in elemento:
                    
                    if subelemento.tag=="nombre":
                        #print("--> nombre:" +str(subelemento.text))
                        nombre=str(subelemento.text)
                    elif subelemento.tag=="filas":
                        #print("--> filas:" +str(subelemento.text))
                        filas=subelemento.text
                    elif subelemento.tag=="columnas":
                        #print("--> columnas:" + str(subelemento.text))
                        columnas=subelemento.text
                    else:
                        #print("------imagen cargada------")
                        #print(subelemento.text)
                        img=subelemento.text
                        temp=lista_Ortogonal()
                        lista_Ortogonal.cont=0    
                        i = 0
                        contfila=0
                        contcol=1
                        contvacio=0
                        contlleno=0
                        hora=datetime.now()
                        while i < len(img):
                            char = img[i]
                            if char=="-" or char=="*":
                                if char=="-":
                                    char=" "
                                    contvacio+=1
                                else:
                                    contlleno+=1
                                #print(char + " fila:"+ str(contfila)+ "  columna:"+ str(contcol))
                                temp.agregarNodo(char,contfila)
                                contcol+=1
                            elif char=="\n":
                                #print("ahuevo saltito"+ str(contfila))
                                if img[i+1]!="\n":
                                    contfila+=1
                                    contcol=1
                            i+= 1
                DATOS.InsertarNodo(nombre,filas,columnas,temp)
                REPORTE.InsertarNodo_repo(hora,nombre,contlleno,contvacio)
        finally:
            DATOS.Recorrer()
            REPORTE.gen()
            #DATOS.Cantidad_nodos()
            print("     **************************      ")
            print("            SUCCESSFULLY             ")
            print("     **************************      ")
    #CREANDO VENTANA PRINCIPAL
    root=Tk()
    root.title("Proyecto2_IPC2")
    root.iconbitmap('icono.ico')
    """
    menubar = tk.Menu(root)
    root.config(menu=menubar)
    menubar.add_cascade(label="INICIO")
    menubar.add_cascade(label="OPERACIONES")"""

    rut=StringVar()
    zm=StringVar()
    zm1=StringVar()

    nt=ttk.Notebook(root)
    nt.pack(fill="both",expand="yes")

    s = ttk.Style()
    # Create style used by default for all Frames
    s.configure('TFrame', background='#0044A3')

    #FRAME INICIO
    s.configure('Frame1.TFrame', background='#0044A3')
    V1 = ttk.Frame(nt, style='Frame1.TFrame')
    nt.add(V1, text="INICIO")

    #FRAME CARGAR ARCHIVO
    s.configure('Frame2.TFrame', background='#04BB32')
    V2 = ttk.Frame(nt, style='Frame2.TFrame')
    nt.add(V2, text="CARGAR ARCHIVO")

    Label(V2,textvariable=rut,font="Helvetica 16",bg="#04BB32").place(x=150,y=20)
    rut.set("NO SE HA CARGADO NADA")
    Button(V2,text="SELECCIONAR ARCHIVO",command=DIALOGO).place(x=500, y=20)

    #FRAME OPERACIONES
    s.configure('Frame3.TFrame', background='#BB7004')
    V3 = ttk.Frame(nt, style='Frame3.TFrame')
    nt.add(V3, text="OPERACIONES")

    #Zona de una matriz

    Label(V3,textvariable=zm1,font="Helvetica 16",bg="#BB7004").place(x=150,y=20)
    zm1.set("CON UNA MATRIZ")
    #opciones1
    Button(V3,text="ROTACION HORIZONTAL",font="Helvetica 14", command=OP1).place(x=80, y=80)
    Button(V3,text="ROTACION VERTICAL",font="Helvetica 14", command=OP2).place(x=80, y=130)
    Button(V3,text="TRANSPUESTA",font="Helvetica 14",command=OP3).place(x=80, y=180)
    Button(V3,text="LIMPIAR ZONA",font="Helvetica 14",command=OP4).place(x=80, y=230)
    Button(V3,text="AGREGAR LINEA HORIZONTAL",font="Helvetica 14",command=OP5).place(x=80, y=280)
    Button(V3,text="AGREGAR LINEA VERTICAL",font="Helvetica 14",command=OP6).place(x=80, y=330)
    Button(V3,text="AGREGAR RECTANGULO",font="Helvetica 14",command=OP7).place(x=80, y=380)
    Button(V3,text="AGREGAR TRIANGULO RECTANGULO",font="Helvetica 14",command=OP8).place(x=80, y=430)
    
    #Zona de dos matrices
    Label(V3,textvariable=zm,font="Helvetica 16",bg="#BB7004").place(x=650,y=20)
    zm.set("CON DOS MATRICES")

    #opciones1
    Button(V3,text="UNIÓN",font="Helvetica 14").place(x=600, y=80)
    Button(V3,text="INTERSECCIÓN",font="Helvetica 14").place(x=600, y=130)
    Button(V3,text="DIFERENCIA",font="Helvetica 14").place(x=600, y=180)
    Button(V3,text="DIFERENCIA SIMÉTRICA",font="Helvetica 14").place(x=600, y=230)
    
    #FRAME REPORTES
    s.configure('Frame4.TFrame', background='#04BBAE')
    V4 = ttk.Frame(nt, style='Frame4.TFrame')
    nt.add(V4, text="REPORTES")

    #FRAME AYUDA
    s.configure('Frame5.TFrame', background='#7104BB')
    V5 = ttk.Frame(nt, style='Frame5.TFrame')
    nt.add(V5, text="AYUDA")

    root.geometry("1000x600")
    root.mainloop()
    
    
    
CREAR_INTERFAZ()

