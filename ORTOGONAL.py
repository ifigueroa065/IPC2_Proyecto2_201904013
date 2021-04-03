from tkinter import *
import os
from tkinter import ttk
import tkinter.filedialog
import tkinter as tk
import xml.etree.ElementTree as ET
class NODO():
    def __init__(self,pix):
        self.pix=pix
        self.top=None
        self.bot=None
        self.left=None
        self.right=None

class lista_Ortogonal():
    cont=0
    def __init__(self):
        self.cabeza=None
    def estaVacia(self):
        return self.cabeza==None
    def agregarNodo(self,pix,fila):
        if self.estaVacia():
            #empieza a crear una fila
            tempNodo=NODO(pix)
            self.cabeza=tempNodo
            lista_Ortogonal.cont+=1
            #print(lista_Ortogonal.cont)
        else:
            aux=self.cabeza

            #recorrido vertical
            while aux.bot!=None:
                aux=aux.bot
            
            if lista_Ortogonal.cont !=fila:
                #print(lista_Ortogonal.cont)
                lista_Ortogonal.cont+=1
                #print(lista_Ortogonal.cont)
                tempNodo=NODO(pix)

                #creando una nueva fila
                aux.bot=tempNodo    #apunta abajo
                tempNodo.top=aux    #apunta arriba    
            else: 
                #recorrido horizontal
                while aux.right!=None:
                    aux=aux.right

                #agregando nodo en una fila    
                tempNodo=NODO(pix)
                aux.right=tempNodo
                tempNodo.left=aux

                #si el nodo es de una fila <> a la principal
                if lista_Ortogonal.cont>1:
                    #se crea 2do nodo auxiliar
                    aux2=aux.top.right
                    aux2.bot=tempNodo
                    tempNodo.top=aux2
    
    def mostrarLista(self):
        contcol=1
        contfila=1
        aux=self.cabeza
        img=""
        while aux.bot !=None or aux.right!=None:
            img+=aux.pix
            if aux.right !=None:
                aux=aux.right
                contcol+=1
            else:
                contfila+=1
                contcol=1

                #imprimo la fila que leí
                print(img)
                if aux.bot!=None:
                    img=""
                    aux=aux.bot
                    while aux.left!=None:
                        aux=aux.left
        img+=aux.pix
        print(img)
        print("hay "+ str(contcol)+ "columnas")
        print("hay "+ str(contfila)+ " filas")
    
    def generar_img_original(self,name,fila,columna):
        with open("matrix.dot", mode="w",encoding="utf-8") as o:
            o.write("""digraph G {\n 
                subgraph cluster1 {\n 
                node [  shape = \"box\" ]
                a0 [ label= <
                <TABLE border=\"1\" cellspacing= \"1\" cellpadding=\"5\">
                        """)
            i=1
            j=0
            
            if j==0:
                o.write("<TR>")
                o.write("""<TD border=\"2\">"""+name+"""</TD>""")
                while i<=int(columna):
                    o.write("""
                                    <TD border=\"2\">"""+str(i)+"""</TD>
                                    
                                    """)
                    i+=1
                i=1
                o.write("</TR>")
            k=1
            aux=self.cabeza
            o.write("<TR>")
            o.write("""<TD border=\"2\">"""+str(k)+"""</TD>""")
            while aux.bot !=None or aux.right!=None:
                o.write("""<TD border=\"2\">"""+aux.pix+"""</TD>\n""")
                if aux.right !=None:
                    aux=aux.right
                else:
                    o.write("</TR>\n")
                    k+=1
                    o.write("<TR>")
                    o.write("""<TD border=\"2\">"""+str(k)+"""</TD>""")
                    #imprimo la fila que leí
                    if aux.bot!=None:
                        img=""
                        aux=aux.bot
                        while aux.left!=None:
                            aux=aux.left
            o.write("""<TD border=\"2\">"""+aux.pix+"""</TD>\n""")
            o.write("</TR>\n")
            img+=aux.pix
            o.write("""
                    
                    </TABLE>>];\n

                    }\n

                    }\n"""); 
               
        os.system('dot -Tpng matrix.dot -o matrix.png');  
        
        print("     **************************      ")
        print("            SUCCESSFULLY             ")
        print("     **************************      ")

    def generar_img(self):
        with open("matrix.dot", mode="w",encoding="utf-8") as o:
            o.write("""digraph G {\n 
                subgraph cluster1 {\n 
                node [  shape = \"box\" ]
                a0 [ label= <
                <TABLE border=\"1\" cellspacing= \"1\" cellpadding=\"5\">
                        """)
            aux=self.cabeza
            img=""
            o.write("<TR>")
            while aux.bot !=None or aux.right!=None:
                o.write("""<TD border=\"2\">"""+aux.pix+"""</TD>\n""")
                if aux.right !=None:
                    aux=aux.right
                else:
                    o.write("</TR>\n")
                    o.write("<TR>")
                    #imprimo la fila que leí
                    if aux.bot!=None:
                        img=""
                        aux=aux.bot
                        while aux.left!=None:
                            aux=aux.left
            o.write("""<TD border=\"2\">"""+aux.pix+"""</TD>\n""")
            o.write("</TR>\n")
            img+=aux.pix
            

            o.write("""
                    
                        
                    
                    </TABLE>>];\n

                    }\n

                    }\n"""); 
               
        os.system('dot -Tpng matrix.dot -o matrix.png');  
        
        print("     **************************      ")
        print("            SUCCESSFULLY             ")
        print("     **************************      ")
