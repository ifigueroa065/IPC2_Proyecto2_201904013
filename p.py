from tkinter import *
from tkinter import ttk
import tkinter.filedialog
import tkinter as tk
import xml.etree.ElementTree as ET

def boto1():
    print("mestoy ejecutando")


def CREAR_INTERFAZ():
    def DIALOGO():
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
            print("--------Todos los atributos--------")
            for elemento in a:
                for subelemento in elemento:
                    if subelemento.tag=="nombre":
                        print("--> nombre:" +str(subelemento.text))
                    elif subelemento.tag=="filas":
                        print("--> filas:" +str(subelemento.text))
                    elif subelemento.tag=="columnas":
                        print("--> columnas:" + str(subelemento.text))
                    else:
                        print("------imagen cargada------")
                        print(subelemento.text)

        finally:
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

    Label(V2,textvariable=rut,font="Helvetica 16").place(x=150,y=20)
    rut.set("NO SE HA CARGADO NADA")
    Button(V2,text="SELECCIONAR ARCHIVO",command=DIALOGO).place(x=500, y=20)

    #FRAME OPERACIONES
    s.configure('Frame3.TFrame', background='#BB7004')
    V3 = ttk.Frame(nt, style='Frame3.TFrame')
    nt.add(V3, text="OPERACIONES")

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

