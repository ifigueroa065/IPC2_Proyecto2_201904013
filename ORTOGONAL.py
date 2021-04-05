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
    def setdato(self,pix):
        self.pix=pix

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
        print("---------MATRIX---------")
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
        """print("hay "+ str(contcol)+ "columnas")
        print("hay "+ str(contfila)+ " filas")"""

    def mostrarLista_Horizontal(self):
        contcol=1
        contfila=1
        aux=self.cabeza
        img=""
        print("---------ROTACION HORIZONTAL---------")
        while aux.bot!=None:
            aux=aux.bot
        
        while aux.top !=None or aux.right!=None:
            img+=aux.pix
            if aux.right !=None:
                aux=aux.right
                contcol+=1
            else:
                contfila+=1
                contcol=1

                #imprimo la fila que leí
                print(img)
                if aux.top!=None:
                    img=""
                    aux=aux.top
                    while aux.left!=None:
                        aux=aux.left
        img+=aux.pix
        print(img)
    
    def mostrarLista_Vertical(self):
        aux=self.cabeza
        img=""
        print("---------ROTACION VERTICAL---------")
        
        while aux.right!=None:
            aux=aux.right
        
        while aux.bot !=None or aux.left!=None:
            img+=aux.pix
            if aux.left !=None:
                aux=aux.left
            else:
                #imprimo la fila que leí
                print(img)
                if aux.bot!=None:
                    img=""
                    aux=aux.bot
                    while aux.right!=None:
                        aux=aux.right
        img+=aux.pix
        print(img)

    def mostrarLista_Transpuesta(self):
        aux=self.cabeza
        img=""
        print("---------TRANSPUESTA---------")
        
        while aux.bot !=None or aux.right!=None:
            img+=aux.pix
            if aux.bot !=None:
                aux=aux.bot
            else:
                #imprimo la fila que leí
                print(img)
                if aux.right!=None:
                    img=""
                    aux=aux.right
                    while aux.top!=None:
                        aux=aux.top
        img+=aux.pix
        print(img)
        
    def agregarLineaHorizontal(self,fila,columna,No):
        k=1
        s=1
        aux=self.cabeza
        img=""
        cox=0
        condicion=True
        #CONTANDO FILAS Y COLUMNAS
        while aux.bot !=None or aux.right!=None:
            if aux.right !=None:
                aux=aux.right
                k+=1
            else:
                s+=1
                k=1
                if aux.bot!=None:
                    aux=aux.bot
                    while aux.left!=None:
                        aux=aux.left
        res=columna+No-1
        if res<=k and fila<s: #valindando parámetros
            contcol=1
            contfila=1
            aux=self.cabeza
            img=""
            cox=0
            condicion=True
            print("---------AGREGANDO LINEA HORIZONTAL---------")
            while aux.bot !=None or aux.right!=None:
                #print(aux.pix+ " fila:"+ str(contfila)+ " columna:"+ str(contcol))
                if contcol==columna and contfila==fila:
                    #aqui inicio
                    aux.pix="s"
                    cox+=1
                    img+=aux.pix
                    condicion=False
                    #print(cox)
                else:
                    img+=aux.pix

                if aux.right !=None and condicion==True:
                    aux=aux.right
                    contcol+=1
                elif aux.right !=None and condicion==False:
                    #print(cox)
                    aux=aux.right
                    contcol+=1
                    if cox<No:
                        aux.pix="s"
                        cox+=1
                        condicion=False
                    else:
                        condicion=True  
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
        else:
            print("ahuevo errorcito")

    def agregarLineaVertical(self,fila,columna,No):
        k=1
        s=1
        aux=self.cabeza
        img=""
        #CONTANDO FILAS Y COLUMNAS
        while aux.bot !=None or aux.right!=None:
            if aux.right !=None:
                aux=aux.right
                k+=1
            else:
                s+=1
                k=1
                if aux.bot!=None:
                    aux=aux.bot
                    while aux.left!=None:
                        aux=aux.left
        res=fila+No-1
        print("---------LINEA VERTICAL---------")
        if res<=s and columna<=k: #valindando parámetros
            contcol=1
            contfila=1
            aux=self.cabeza
            img=""
            
            coy=1
            while aux.bot !=None or aux.right!=None:
                
                if contcol==columna  and contfila==fila:
                    #aqui inicio
                    if coy<=No:
                        aux.pix="s"
                        img+=aux.pix
                        coy+=1
                        fila+=1
                    else:
                        img+=aux.pix

                else:
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
        else:
            print("ahuevo errorcito")

    def limpiar_zona(self,xo,yo,x,y):
        k=1
        s=1
        aux=self.cabeza
        #CONTANDO FILAS Y COLUMNAS
        while aux.bot !=None or aux.right!=None:
            if aux.right !=None:
                aux=aux.right
                k+=1
            else:
                s+=1
                k=1
                if aux.bot!=None:
                    aux=aux.bot
                    while aux.left!=None:
                        aux=aux.left
        res=y-yo+1
        
        print("---------LIMPIANDO ZONA---------")
        co1=False
        co2=False
        
        if xo<=s and yo<=k:
            co1=True
        if x<=s and y<=k:
            co2=True
            
        if co1 and co2:
            auxiliar=self.cabeza
            DX=x-xo
            DY=y-yo
            
            nodo_inicial=None
            encontrado=False

            for i in range(1,k+1):
                aux2=auxiliar
                for j in range(1,s+1):
                    if i==xo and j==yo:
                        #encuentro el nodo
                        nodo_inicial=aux2
                        encontrado=True
                        break
                    aux2=aux2.right
                if encontrado:
                    break
                auxiliar=auxiliar.bot
            
            for i in range(0,DX+1):
                node=nodo_inicial
                for j in range(0,DY+1):
                    node.pix=" "
                    node=node.right
                nodo_inicial=nodo_inicial.bot
            self.mostrarLista()
        else:
            print("ahueevo errocito")
        
    def agregar_rectangulo(self,xo,yo,a,b):
        k=1 #COLUMNAS
        s=1 #FILAS
        aux=self.cabeza
        #CONTANDO FILAS Y COLUMNAS
        while aux.bot !=None or aux.right!=None:
            if aux.right !=None:
                aux=aux.right
                k+=1
            else:
                s+=1
                k=1
                if aux.bot!=None:
                    aux=aux.bot
                    while aux.left!=None:
                        aux=aux.left
        if xo<=k and yo<=s and a<=s and b<=k: #validando parámetros
            auxiliar=self.cabeza
            nodo_inicial=None
            node=None
            found=False

            for i in range(1,k+1):
                aux2=auxiliar
                for j in range(1,s+1):
                    if i==xo and j==yo:
                        #encuentro el nodo
                        nodo_inicial=aux2
                        nodo_aux=aux2
                        found=True
                        break
                    aux2=aux2.right
                if found:
                    break
                auxiliar=auxiliar.bot
            #a=altura
            #b=ancho
            for i in range(0,a-1):
                nodo_inicial.pix="*"
                nodo_inicial= nodo_inicial.bot
            node=nodo_inicial
            for i in range(0,b):
                node.pix="*"
                nodo_aux.pix="*"
                    
                node2=nodo_aux
                node=node.right
                nodo_aux=nodo_aux.right
            for i in range(0,a-1):
                node2.pix="*"
                node2=node2.bot

            #luego de agregar la  muestro     
            self.mostrarLista()
        else:
            print("pues no mi ciela")

    def agregar_triangulo(self,xo,yo,lado):
        k=1 #COLUMNAS
        s=1 #FILAS
        aux=self.cabeza
        #CONTANDO FILAS Y COLUMNAS
        while aux.bot !=None or aux.right!=None:
            if aux.right !=None:
                aux=aux.right
                k+=1
            else:
                s+=1
                k=1
                if aux.bot!=None:
                    aux=aux.bot
                    while aux.left!=None:
                        aux=aux.left

        if xo<=k and yo<=s and lado<=s and lado<=k: #validando parámetros
            auxiliar=self.cabeza
            nodo_inicial=None
            node=None
            found=False

            for i in range(1,k+1):
                aux2=auxiliar
                for j in range(1,s+1):
                    if i==xo and j==yo:
                        #encuentro el nodo
                        nodo_inicial=aux2
                        nodo_aux=aux2
                        found=True
                        break
                    aux2=aux2.right
                if found:
                    break
                auxiliar=auxiliar.bot
            #a=altura
            #b=ancho
            for i in range(0,lado-1):
                nodo_inicial.pix="*"
                nodo_inicial= nodo_inicial.bot
            node=nodo_inicial

            for i in range(0,lado):
                node.pix="*"
                node=node.right

            for i in range(0,lado-1):
                nodo_aux=nodo_aux.bot
                nodo_aux=nodo_aux.right
                nodo_aux.pix="*"
            #luego de agregar la  muestro     
            self.mostrarLista()
        else:
            print("pues no mi ciela")
    

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
        print("        IMAGEN  SUCCESSFULLY             ")
        print("     **************************      ")

    def generar_img_horizontal(self,name,fila,columna):
        with open("matrix_horizontal.dot", mode="w",encoding="utf-8") as o:
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
            while aux.bot!=None:
                aux=aux.bot
            while aux.top !=None or aux.right!=None:
                o.write("""<TD border=\"2\">"""+aux.pix+"""</TD>\n""")
                if aux.right !=None:
                    aux=aux.right
                else:
                    o.write("</TR>\n")
                    k+=1
                    o.write("<TR>")
                    o.write("""<TD border=\"2\">"""+str(k)+"""</TD>""")
                    #imprimo la fila que leí
                    if aux.top!=None:
                        img=""
                        aux=aux.top
                        while aux.left!=None:
                            aux=aux.left
            o.write("""<TD border=\"2\">"""+aux.pix+"""</TD>\n""")
            o.write("</TR>\n")
            img+=aux.pix
            o.write("""
                    
                    </TABLE>>];\n

                    }\n

                    }\n"""); 
               
        os.system('dot -Tpng matrix_horizontal.dot -o matrix_horizontal.png');  
        
        print("     **************************      ")
        print("        IMAGEN  SUCCESSFULLY             ")
        print("     **************************      ")

    def generar_img_vertical(self,name,fila,columna):
        with open("matrix_vertical.dot", mode="w",encoding="utf-8") as o:
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
            while aux.right!=None:
                aux=aux.right
            while aux.bot !=None or aux.left!=None:
                o.write("""<TD border=\"2\">"""+aux.pix+"""</TD>\n""")
                if aux.left !=None:
                    aux=aux.left
                else:
                    o.write("</TR>\n")
                    k+=1
                    o.write("<TR>")
                    o.write("""<TD border=\"2\">"""+str(k)+"""</TD>""")
                    #imprimo la fila que leí
                    if aux.bot!=None:
                        img=""
                        aux=aux.bot
                        while aux.right!=None:
                            aux=aux.right
            o.write("""<TD border=\"2\">"""+aux.pix+"""</TD>\n""")
            o.write("</TR>\n")
            img+=aux.pix
            o.write("""
                    
                    </TABLE>>];\n

                    }\n

                    }\n"""); 
               
        os.system('dot -Tpng matrix_vertical.dot -o matrix_vertical.png');  
        
        print("     **************************      ")
        print("        IMAGEN  SUCCESSFULLY             ")
        print("     **************************      ")

    def generar_img_transpuesta(self,name,fila,columna):
        with open("matrix_transpuesta.dot", mode="w",encoding="utf-8") as o:
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
                if aux.bot !=None:
                    aux=aux.bot
                else:
                    o.write("</TR>\n")
                    k+=1
                    o.write("<TR>")
                    o.write("""<TD border=\"2\">"""+str(k)+"""</TD>""")
                    #imprimo la fila que leí
                    if aux.right!=None:
                        img=""
                        aux=aux.right
                        while aux.top!=None:
                            aux=aux.top
            o.write("""<TD border=\"2\">"""+aux.pix+"""</TD>\n""")
            o.write("</TR>\n")
            img+=aux.pix
            o.write("""
                    
                    </TABLE>>];\n

                    }\n

                    }\n"""); 
               
        os.system('dot -Tpng matrix_transpuesta.dot -o matrix_transpuesta.png');  
        
        print("     **************************      ")
        print("        IMAGEN  SUCCESSFULLY             ")
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
        print("         IMAGEN SUCCESSFULLY             ")
        print("     **************************      ")

    


prueba=lista_Ortogonal()
prueba.agregarNodo("#",1)
prueba.agregarNodo("#",1)
prueba.agregarNodo("#",1)
prueba.agregarNodo("#",1)

prueba.agregarNodo("-",2)
prueba.agregarNodo("#",2)
prueba.agregarNodo("-",2)
prueba.agregarNodo("#",2)

prueba.agregarNodo("#",3)
prueba.agregarNodo("#",3)
prueba.agregarNodo("#",3)
prueba.agregarNodo("#",3)

prueba.agregarNodo("#",4)
prueba.agregarNodo("#",4)
prueba.agregarNodo("#",4)
prueba.agregarNodo("#",4)

prueba.mostrarLista()
#prueba.mostrarLista_Horizontal()
#prueba.mostrarLista_Vertical()
#prueba.mostrarLista_Transpuesta()
#prueba.agregarLineaHorizontal(2,1,2)
#prueba.agregarLineaVertical(1,4,3)
#prueba.limpiar_zona(2,2,3,3)
#prueba.agregar_rectangulo(1,1,4,2)
prueba.agregar_triangulo(1,1,5)