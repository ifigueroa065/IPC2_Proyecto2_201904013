from tkinter import *
import os
from datetime import datetime
import webbrowser

from tkinter import messagebox
from tkinter import ttk
import tkinter.filedialog
import tkinter as tk
import xml.etree.ElementTree as ET
from PIL import ImageTk, Image
from Circular import ListaCircular
from ORTOGONAL import lista_Ortogonal

DATOS= ListaCircular()
REPORTE=ListaCircular()
ERRORES=ListaCircular()
OPERACIONES=ListaCircular()
def CREAR_INTERFAZ():
    global OPERACIONES,ERRORES
    def OP1():
        global OPERACIONES,ERRORES
        def ROTAR_IMG():    
            name=desplegable.get()
            print("HOLA TOY ROTANDO")
            hora=datetime.now()
            operacion="ROTACION HORIZONTAL"
            OPERACIONES.InsertarNodo_OP(hora,operacion,name)
            DATOS.buscar(name)
            
            DATOS.buscar_y_rotar_horizontal(name)
            imagen2=Image.open("matrix_horizontal.png")
            resized=imagen2.resize((600,500),Image.ANTIALIAS)
            new=ImageTk.PhotoImage(resized)
            s2=Label(miframe,image=new)
            s2.place(x=50,y=100).pack()

            
        L1=StringVar()
        widget=StringVar()  
        op1=Toplevel()

        op1.title("ROTACION HORIZONTAL")
        op1.iconbitmap('icono.ico')
        op1.geometry("1300x750")
        op1.config(bg="#0044A3")

        miframe=Frame(op1,width=1000,height=1000)
        miframe.config(bg="#0044A3")
        miframe.pack(fill="both",expand="True")
        Label(miframe,textvariable=L1,font="Helvetica 16",bg="#0044A3").place(x=30,y=20)
        L1.set("Seleccione una matriz")
        Label(miframe,textvariable=widget,font="Helvetica 16",bg="#0044A3").place(x=30,y=70)
        #frame.config(bg="#0044A3",width="400", height="400")
        desplegable=ttk.Combobox(miframe,width=20,font="Helvetica 14",state="readonly")
        desplegable.place(x=250,y=20)
        desplegable['values']=DATOS.NOMBRES()
        Button(miframe,text="CARGAR IMAGEN",command=ROTAR_IMG,font="Helvetica 12",bg="gold").place(x=500, y=20)
        
        """imageno=Image.open("matrix.png")
        imagen2=Image.open("matrix_horizontal.png")
        resized2=imageno.resize((400,400),Image.ANTIALIAS)
        resized=imagen2.resize((400,400),Image.ANTIALIAS)
        new1=ImageTk.PhotoImage(resized2)
        new=ImageTk.PhotoImage(resized)
        s1=Label(miframe,image=new1)
        s1.place(x=700,y=100)
        s2=Label(miframe,image=new)
        s2.place(x=50,y=100)"""
        
        op1.mainloop()

    def OP2():
        global OPERACIONES,ERRORES
        def  ROTAR_IMG():
            name=desplegable.get()
            print("HOLA SOY LA VERTICAL")
            DATOS.buscar(name)
            hora=datetime.now()
            operacion="ROTACION VERTICAL"
            OPERACIONES.InsertarNodo_OP(hora,operacion,name)
            DATOS.buscar_y_rotar_vertical(name)
            imagen2=Image.open("matrix_vertical.png")
            resized=imagen2.resize((600,500),Image.ANTIALIAS)
            new=ImageTk.PhotoImage(resized)
            s3=Label(miframe1,image=new)
            s3.place(x=50,y=100).pack()
            
        
        L2=StringVar()
        op2=Toplevel()
        op2.title("ROTACION VERTICAL")
        op2.iconbitmap('icono.ico')
        op2.geometry("1200x700")
        op2.config(bg="#0044A3")

        miframe1=Frame(op2,width=1000,height=1000)
        miframe1.config(bg="#0044A3")
        miframe1.pack(fill="both",expand="True")
        Label(miframe1,textvariable=L2,font="Helvetica 16",bg="#0044A3").place(x=30,y=20)
        L2.set("Seleccione una matriz")
        #frame.config(bg="#0044A3",width="400", height="400")
        desplegable=ttk.Combobox(miframe1,width=20,font="Helvetica 14")
        desplegable.place(x=250,y=20)
        desplegable['values']=DATOS.NOMBRES()
        Button(miframe1,text="CARGAR IMAGEN",command=ROTAR_IMG,font="Helvetica 12",bg="gold").place(x=500, y=20)
        op2.mainloop()
    
    def OP3():
        global OPERACIONES,ERRORES
        def ROTAR_IMG():    
            name=desplegable.get()
            print("HOLA SOY LA TRANSPUESTA")
            DATOS.buscar(name)
            if DATOS.buscar_transpuesta(name)==True:
                hora=datetime.now()
                operacion="TRANSPUESTA"
                OPERACIONES.InsertarNodo_OP(hora,operacion,name)
                DATOS.buscar_transpuesta(name)
                imagen2=Image.open("matrix_transpuesta.png")
                resized=imagen2.resize((600,500),Image.ANTIALIAS)
                new=ImageTk.PhotoImage(resized)
                s2=Label(miframe,image=new)
                s2.place(x=50,y=100).pack()
                
            else:
                hora=datetime.now()
                ERRORES.InsertarNodo_ERROR(hora,"La matriz no es cuadrada")
                messagebox.showinfo(message="La matriz debe ser cuadrada", title="ERROR")

        L1=StringVar()
        widget=StringVar()  
        op3=Toplevel()

        op3.title("TRANSPUESTA")
        op3.iconbitmap('icono.ico')
        op3.geometry("1200x700")
        op3.config(bg="#0044A3")

        miframe=Frame(op3,width=1000,height=1000)
        miframe.config(bg="#0044A3")
        miframe.pack(fill="both",expand="True")

        Label(miframe,textvariable=L1,font="Helvetica 16",bg="#0044A3").place(x=30,y=20)
        L1.set("Seleccione una matriz")
        Label(miframe,textvariable=widget,font="Helvetica 16",bg="#0044A3").place(x=30,y=70)
        #frame.config(bg="#0044A3",width="400", height="400")
        desplegable=ttk.Combobox(miframe,width=20,font="Helvetica 14",state="readonly")
        desplegable.place(x=250,y=20)
        desplegable['values']=DATOS.NOMBRES()

        Button(miframe,text="CARGAR IMAGEN",command=ROTAR_IMG,font="Helvetica 12",bg="gold").place(x=500, y=20)
        op3.mainloop()

    def OP4():
        global OPERACIONES,ERRORES
        def ROTAR_IMG():    
            #obteniendo valores
            name=desplegable.get()
            Po=xo.get()
            Qo=yo.get()
            P=x.get()
            Q=y.get()
            if Po!=0 and Qo!=0 and P!=0 and Q!=0:
                print("HOLA TOY LIMPIANDO")
                DATOS.buscar(name)
                if DATOS.buscar_y_limpiar(name,Po,Qo,P,Q)==True:
                    hora=datetime.now()
                    operacion="LIMPIAR ZONA"
                    OPERACIONES.InsertarNodo_OP(hora,operacion,name)
                    DATOS.buscar_y_limpiar(name,Po,Qo,P,Q)
                    imagen2=Image.open("auxiliar.png")
                    resized=imagen2.resize((600,500),Image.ANTIALIAS)
                    new=ImageTk.PhotoImage(resized)
                    s2=Label(miframe,image=new)
                    s2.place(x=50,y=100).pack()
                else:
                    hora=datetime.now()
                    ERRORES.InsertarNodo_ERROR(hora,"Los datos sobrepasan los limites")
                    messagebox.showinfo(message="Los datos sobrepasan los limites", title="ERROR") 

            else:
                messagebox.showinfo(message="Debe llenar todos los campos", title="ERROR")

            
            
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

        miframe=Frame(op4,width=1000,height=1000)
        miframe.config(bg="#0044A3")
        miframe.pack(fill="both",expand="True")

        Label(miframe,textvariable=L1,font="Helvetica 16",bg="#0044A3").place(x=30,y=20)
        L1.set("Seleccione una matriz")

        Label(miframe,textvariable=l2,font="Helvetica 12",bg="#0044A3").place(x=750,y=100)
        l2.set("Xo")
        Label(miframe,textvariable=l3,font="Helvetica 12",bg="#0044A3").place(x=750,y=140)
        l3.set("Yo")
        Label(miframe,textvariable=l4,font="Helvetica 12",bg="#0044A3").place(x=750,y=250)
        l4.set("X")
        Label(miframe,textvariable=l5,font="Helvetica 12",bg="#0044A3").place(x=750,y=290)
        l5.set("Y")

        #frame.config(bg="#0044A3",width="400", height="400")
        desplegable=ttk.Combobox(miframe,width=20,font="Helvetica 14",state="readonly")
        desplegable.place(x=250,y=20)
        desplegable['values']=DATOS.NOMBRES()
        
        Entry(miframe,textvariable=xo,font="Helvetica 12").place(x=790,y=100)
        Entry(miframe,textvariable=yo,font="Helvetica 12").place(x=790,y=140)
        Entry(miframe,textvariable=x,font="Helvetica 12").place(x=790,y=250)
        Entry(miframe,textvariable=y,font="Helvetica 12").place(x=790,y=290)

        
        Button(miframe,text="CARGAR IMAGEN",command=ROTAR_IMG,font="Helvetica 12",bg="gold").place(x=500, y=20)
        op4.mainloop()
    
    def OP5():
        global OPERACIONES,ERRORES
        def  ROTAR_IMG():
            #obteniendo valores

            name=desplegable.get()
            Po=xo.get()
            Qo=yo.get()
            No=no.get()
            if Po!=0 and Qo!=0 and No!=0:
                print("HOLA TOY AGREGANDO FILA HORIZONTAL")
                DATOS.buscar(name)
                if DATOS.buscar_e_insertar_lh(name,Po,Qo,No)==True:
                    hora=datetime.now()
                    operacion="AGREGAR FILA HORIZONTAL"
                    OPERACIONES.InsertarNodo_OP(hora,operacion,name)

                    DATOS.buscar_e_insertar_lh(name,Po,Qo,No)
                    imagen2=Image.open("auxiliar.png")
                    resized=imagen2.resize((600,500),Image.ANTIALIAS)
                    new=ImageTk.PhotoImage(resized)
                    s2=Label(miframe,image=new)
                    s2.place(x=50,y=100).pack()
    
                else:
                    hora=datetime.now()
                    ERRORES.InsertarNodo_ERROR(hora,"Los datos sobrepasan los limites")    
                    messagebox.showinfo(message="Los datos sobrepasan los limites", title="ERROR")

            else:
                messagebox.showinfo(message="Debe llenar todos los campos", title="ERROR")
            
        L1=StringVar()

        l2=StringVar()
        l3=StringVar()
        l4=StringVar()
        l5=StringVar()
  
        op5=Toplevel()
        
        xo=IntVar()
        yo=IntVar()
        no=IntVar()
        
        op5.title("INSERTAR LINEA HORIZONTAL")
        op5.iconbitmap('icono.ico')
        op5.geometry("1200x700")
        op5.config(bg="#0044A3")

        miframe=Frame(op5,width=1000,height=1000)
        miframe.config(bg="#0044A3")
        miframe.pack(fill="both",expand="True")

        Label(miframe,textvariable=L1,font="Helvetica 16",bg="#0044A3").place(x=30,y=20)
        L1.set("Seleccione una matriz")

        Label(miframe,textvariable=l2,font="Helvetica 12",bg="#0044A3").place(x=750,y=100)
        l2.set("Xo")
        Label(miframe,textvariable=l3,font="Helvetica 12",bg="#0044A3").place(x=750,y=140)
        l3.set("Yo")
        Label(miframe,textvariable=l4,font="Helvetica 14",bg="#0044A3").place(x=790,y=250)
        l4.set("No. Elementos")

        #frame.config(bg="#0044A3",width="400", height="400")
        desplegable=ttk.Combobox(miframe,width=20,font="Helvetica 14",state="readonly")
        desplegable.place(x=250,y=20)
        desplegable['values']=DATOS.NOMBRES()
        
        Entry(miframe,textvariable=xo,font="Helvetica 12").place(x=790,y=100)
        Entry(miframe,textvariable=yo,font="Helvetica 12").place(x=790,y=140)
        
        Entry(miframe,textvariable=no,font="Helvetica 12").place(x=790,y=290)

        Button(miframe,text="CARGAR IMAGEN",command=ROTAR_IMG,font="Helvetica 12",bg="gold").place(x=500, y=20)
        op5.mainloop()

    def OP6():
        global OPERACIONES,ERRORES
        def  ROTAR_IMG():
            #obteniendo valores
            name=desplegable.get()
            Po=xo.get()
            Qo=yo.get()
            No=no.get()
            if Po!=0 and Qo!=0 and No!=0:
                print("HOLA TOY AGREGANDO FILA VERTICAL")
                DATOS.buscar(name)
                if  DATOS.buscar_e_insertar_lv(name,Po,Qo,No)==True:
                    hora=datetime.now()
                    operacion="AGREGAR FILA VERTICAL"
                    OPERACIONES.InsertarNodo_OP(hora,operacion,name)

                    DATOS.buscar_e_insertar_lv(name,Po,Qo,No)
                    
                    imagen2=Image.open("auxiliar.png")
                    resized=imagen2.resize((600,500),Image.ANTIALIAS)
                    new=ImageTk.PhotoImage(resized)
                    s2=Label(miframe,image=new)
                    s2.place(x=50,y=100).pack()
                else:
                    hora=datetime.now()
                    ERRORES.InsertarNodo_ERROR(hora,"Los datos sobrepasan los limites")
                    messagebox.showinfo(message="Los datos sobrepasan los limites", title="ERROR") 
            else:
                messagebox.showinfo(message="Debe llenar todos los campos", title="ERROR")
        
        L1=StringVar()

        l2=StringVar()
        l3=StringVar()
        l4=StringVar()
        l5=StringVar()
  
        op6=Toplevel()
        
        xo=IntVar()
        yo=IntVar()
        no=IntVar()
        
        op6.title("INSERTAR LINEA VERTICAL")
        op6.iconbitmap('icono.ico')
        op6.geometry("1200x700")
        op6.config(bg="#0044A3")

        miframe=Frame(op6,width=1000,height=1000)
        miframe.config(bg="#0044A3")
        miframe.pack(fill="both",expand="True")

        Label(miframe,textvariable=L1,font="Helvetica 16",bg="#0044A3").place(x=30,y=20)
        L1.set("Seleccione una matriz")

        Label(miframe,textvariable=l2,font="Helvetica 12",bg="#0044A3").place(x=750,y=100)
        l2.set("Xo")
        Label(miframe,textvariable=l3,font="Helvetica 12",bg="#0044A3").place(x=750,y=140)
        l3.set("Yo")
        Label(miframe,textvariable=l4,font="Helvetica 14",bg="#0044A3").place(x=790,y=250)
        l4.set("No. Elementos")

        #frame.config(bg="#0044A3",width="400", height="400")
        desplegable=ttk.Combobox(miframe,width=20,font="Helvetica 14",state="readonly")
        desplegable.place(x=250,y=20)
        desplegable['values']=DATOS.NOMBRES()
        
        Entry(miframe,textvariable=xo,font="Helvetica 12").place(x=790,y=100)
        Entry(miframe,textvariable=yo,font="Helvetica 12").place(x=790,y=140)
        
        Entry(miframe,textvariable=no,font="Helvetica 12").place(x=790,y=290)

    
        Button(miframe,text="CARGAR IMAGEN",command=ROTAR_IMG,font="Helvetica 12",bg="gold").place(x=500, y=20)
        op6.mainloop()
    
    def OP7():
        global OPERACIONES,ERRORES
        def ROTAR_IMG():    
            #obteniendo valores
            name=desplegable.get()
            Po=xo.get()
            Qo=yo.get()
            P=alto.get()
            Q=ancho.get()
            if Po!=0 and Qo!=0 and P!=0 and Q!=0:
                print("HOLA TOY AGREGANDO RECTANGULO")
                DATOS.buscar(name)
                if DATOS.buscar_e_insertar_R(name,Po,Qo,P,Q)==True:
                    hora=datetime.now()
                    operacion="INSERTAR RECTÁNGULO"
                    OPERACIONES.InsertarNodo_OP(hora,operacion,name)

                    DATOS.buscar_e_insertar_R(name,Po,Qo,P,Q)
                    
                    imagen2=Image.open("auxiliar.png")
                    resized=imagen2.resize((600,500),Image.ANTIALIAS)
                    new=ImageTk.PhotoImage(resized)
                    s2=Label(miframe,image=new)
                    s2.place(x=50,y=100).pack()
                    
                else:
                    hora=datetime.now()
                    ERRORES.InsertarNodo_ERROR(hora,"Los datos sobrepasan los limites")
                    messagebox.showinfo(message="Los datos sobrepasan los limites", title="ERROR")
            else:
                messagebox.showinfo(message="Debe llenar todos los campos", title="ERROR")
        L1=StringVar()

        l2=StringVar()
        l3=StringVar()
        l4=StringVar()
        l5=StringVar()
  
        op7=Toplevel()
        
        xo=IntVar()
        yo=IntVar()
        alto=IntVar()
        ancho=IntVar()
        
        op7.title("INSERTAR RECTÁNGULO")
        op7.iconbitmap('icono.ico')
        op7.geometry("1200x700")
        op7.config(bg="#0044A3")

        miframe=Frame(op7,width=1000,height=1000)
        miframe.config(bg="#0044A3")
        miframe.pack(fill="both",expand="True")

        Label(miframe,textvariable=L1,font="Helvetica 16",bg="#0044A3").place(x=30,y=20)
        L1.set("Seleccione una matriz")

        Label(miframe,textvariable=l2,font="Helvetica 12",bg="#0044A3").place(x=750,y=100)
        l2.set("Xo")
        Label(miframe,textvariable=l3,font="Helvetica 12",bg="#0044A3").place(x=750,y=140)
        l3.set("Yo")
        Label(miframe,textvariable=l4,font="Helvetica 12",bg="#0044A3").place(x=750,y=250)
        l4.set("Alto")
        Label(miframe,textvariable=l5,font="Helvetica 12",bg="#0044A3").place(x=750,y=290)
        l5.set("Ancho")

        #frame.config(bg="#0044A3",width="400", height="400")
        desplegable=ttk.Combobox(miframe,width=20,font="Helvetica 14",state="readonly")
        desplegable.place(x=250,y=20)
        desplegable['values']=DATOS.NOMBRES()
        
        Entry(miframe,textvariable=xo,font="Helvetica 12").place(x=790,y=100)
        Entry(miframe,textvariable=yo,font="Helvetica 12").place(x=790,y=140)
        Entry(miframe,textvariable=alto,font="Helvetica 12").place(x=790,y=250)
        Entry(miframe,textvariable=ancho,font="Helvetica 12").place(x=790,y=290)

        Button(miframe,text="CARGAR IMAGEN",command=ROTAR_IMG,font="Helvetica 12",bg="gold").place(x=500, y=20)
        op7.mainloop()

    def OP8():
        def  ROTAR_IMG():
            #obteniendo valores
            name=desplegable.get()
            Po=xo.get()
            Qo=yo.get()
            L=lado.get()
            if Po!=0 and Qo!=0 and L!=0:
                print("HOLA TOY AGREGANDO TRIANGULO RECTANGULO")
                DATOS.buscar(name)
                if DATOS.buscar_e_insertar_TR(name,Po,Qo,L)==True: 
                    hora=datetime.now()
                    operacion="INSERTAR TRIÁNGULO RECTÁNGULO"
                    OPERACIONES.InsertarNodo_OP(hora,operacion,name)

                    DATOS.buscar_e_insertar_TR(name,Po,Qo,L)
                    
                    imagen2=Image.open("auxiliar.png")
                    resized=imagen2.resize((600,500),Image.ANTIALIAS)
                    new=ImageTk.PhotoImage(resized)
                    s2=Label(miframe,image=new)
                    s2.place(x=50,y=100).pack()
                    
                else:
                    hora=datetime.now()
                    ERRORES.InsertarNodo_ERROR(hora,"Los datos sobrepasan los limites")
                    messagebox.showinfo(message="Los datos sobrepasan los limites", title="ERROR")
            else:
                messagebox.showinfo(message="Debe llenar todos los campos", title="ERROR")
            
        L1=StringVar()

        l2=StringVar()
        l3=StringVar()
    
        l4=StringVar()
        op8=Toplevel()
        
        xo=IntVar()
        yo=IntVar()
        lado=IntVar()
        
        op8.title("INSERTAR TRIANGULO RECTANGULO")
        op8.iconbitmap('icono.ico')
        op8.geometry("1200x700")
        op8.config(bg="#0044A3")

        miframe=Frame(op8,width=1000,height=1000)
        miframe.config(bg="#0044A3")
        miframe.pack(fill="both",expand="True")

        Label(miframe,textvariable=L1,font="Helvetica 16",bg="#0044A3").place(x=30,y=20)
        L1.set("Seleccione una matriz")

        Label(miframe,textvariable=l2,font="Helvetica 12",bg="#0044A3").place(x=750,y=100)
        l2.set("Xo")
        Label(miframe,textvariable=l3,font="Helvetica 12",bg="#0044A3").place(x=750,y=140)
        l3.set("Yo")
        Label(miframe,textvariable=l4,font="Helvetica 14",bg="#0044A3").place(x=790,y=250)
        l4.set("Lado")

        #frame.config(bg="#0044A3",width="400", height="400")
        desplegable=ttk.Combobox(miframe,width=20,font="Helvetica 14",state="readonly")
        desplegable.place(x=250,y=20)
        desplegable['values']=DATOS.NOMBRES()
        
        Entry(miframe,textvariable=xo,font="Helvetica 12").place(x=790,y=100)
        Entry(miframe,textvariable=yo,font="Helvetica 12").place(x=790,y=140)
        
        Entry(miframe,textvariable=lado,font="Helvetica 12").place(x=770,y=290)

        Button(miframe,text="CARGAR IMAGEN",command=ROTAR_IMG,font="Helvetica 12",bg="gold").place(x=500, y=20)
        op8.mainloop()


    def ver_reporte():
        global OPERACIONES,ERRORES
        OPERACIONES.CREAR_REPO_OPERACIONES()
        OPERACIONES.recorrer_OP()
        ERRORES.recorrer_ER()
        ERRORES.CREAR_REPO_ERRORES()
        webbrowser.open_new_tab('REGISTRO.html')

    def ver_datos():
        NOMBRES=StringVar()
        APELLIDOS=StringVar()
        CARNET=StringVar()
        verd=Toplevel()

        verd.title("DATOS ESTUDIANTE")
        verd.iconbitmap('icono.ico')
        verd.geometry("300x200")
        verd.config(bg="#0044A3")

        Label(verd,textvariable=NOMBRES,font="Helvetica 16",bg="#0044A3").place(x=30,y=20)
        NOMBRES.set("Marlon Isaí")
        Label(verd,textvariable=APELLIDOS,font="Helvetica 16",bg="#0044A3").place(x=30,y=80)
        APELLIDOS.set("Figueroa Farfán")
        Label(verd,textvariable=CARNET,font="Helvetica 16",bg="#0044A3").place(x=30,y=140)
        CARNET.set("Carnet: 201904013")
        
        
        verd.mainloop()

    def ver_doct():
        webbrowser.open_new_tab('DOCUMENTACION.pdf')

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
        if ruta=="":
            messagebox.showinfo(message="Debe cargar un archivo", title="ERROR")
        else:
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
                REPORTE.CREAR_REPO_REGISTRO()

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
    Button(V2,text="SELECCIONAR ARCHIVO",font="Helvetica 16",command=DIALOGO).place(x=500, y=20)

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
    u1=StringVar()
    s.configure('Frame4.TFrame', background='#04BBAE')
    V4 = ttk.Frame(nt, style='Frame4.TFrame')
    nt.add(V4, text="REPORTES")

    Label(V4,textvariable=u1,font="Helvetica 24",bg="#04BBAE").place(x=410,y=40)
    u1.set("VISUALIZAR REPORTES")

    icorepo=PhotoImage(file="repo.png")
    icorepo.subsample(1,1)
    Button(V4,image=icorepo,command=ver_reporte,font="Helvetica 14",width=400,height=400).place(x=400, y=130)
    
    #FRAME AYUDA
    t1=StringVar()
    t2=StringVar()

    s.configure('Frame5.TFrame', background='#7104BB')
    V5 = ttk.Frame(nt, style='Frame5.TFrame')
    nt.add(V5, text="AYUDA")
    Label(V5,textvariable=t1,font="Helvetica 24",bg="#7104BB").place(x=160,y=40)
    t1.set("INFORMACIÓN")
    Label(V5,textvariable=t2,font="Helvetica 24",bg="#7104BB").place(x=750,y=40)
    t2.set("DOCUMENTACIÓN")

    icoinf=PhotoImage(file="info.png")
    icoinf.subsample(1,1)
    icodoct=PhotoImage(file="doct.png")
    icodoct.subsample(1,1)

    Button(V5,image=icoinf,command=ver_datos,font="Helvetica 14",width=400,height=400).place(x=100, y=130)
    Button(V5,image=icodoct,command=ver_doct,font="Helvetica 14",width=400,height=400).place(x=700, y=130)

    root.geometry("1300x700")
    root.mainloop()
    
    
    
CREAR_INTERFAZ()

