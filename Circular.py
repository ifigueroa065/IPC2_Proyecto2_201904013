from NodoC import Nodo_C
from REPORTE import OPERACION
from REPORTE import OP
from REPORTE import ERROR
from ORTOGONAL import lista_Ortogonal

import os
from datetime import datetime
from tkinter import messagebox
class ListaCircular():
    def __init__(self):
        self.primero=None
        self.ultimo=None
    def Vacia(self):
        return  self.primero==None


    def  InsertarNodo(self,nombre,n,m,datos):
        if self.Vacia():
            self.primero=self.ultimo=Nodo_C(nombre,n,m,datos)
            self.ultimo.siguiente=self.primero
        else:
            aux= self.ultimo
            self.ultimo=aux.siguiente=Nodo_C(nombre,n,m,datos)
            self.ultimo.siguiente=self.primero

    def InsertarNodo_repo(self,hora,nombre,lleno,vacio):
        if self.Vacia():
            self.primero=self.ultimo=OPERACION(hora,nombre,lleno,vacio)
            self.ultimo.siguiente=self.primero
        else:
            aux= self.ultimo
            self.ultimo=aux.siguiente=OPERACION(hora,nombre,lleno,vacio)
            self.ultimo.siguiente=self.primero

    def InsertarNodo_OP(self,hora,operacion,nombre):
        if self.Vacia():
            self.primero=self.ultimo=OP(hora,operacion,nombre)
            self.ultimo.siguiente=self.primero
        else:
            aux= self.ultimo
            self.ultimo=aux.siguiente=OP(hora,operacion,nombre)
            self.ultimo.siguiente=self.primero

    def InsertarNodo_ERROR(self,hora,descripcion):
        if self.Vacia():
            self.primero=self.ultimo=ERROR(hora,descripcion)
            self.ultimo.siguiente=self.primero
        else:
            aux= self.ultimo
            self.ultimo=aux.siguiente=ERROR(hora,descripcion)
            self.ultimo.siguiente=self.primero


    def Recorrer(self):
        aux=self.primero
        while aux:
            print("************************")
            print("nombre:" + aux.nombre + "\nfilas:" + str(aux.filas) + "\nColumnas:" + str(aux.columnas))
            print("-----------------")
            print("MATRIZ CARGADA")
            aux.imagen.mostrarLista()
            aux=aux.siguiente
            if aux==self.primero:
                break
    
    def gen(self):
        aux=self.primero
        while aux:
            print("************************")
            print(str(aux.hora) + "-" + str(aux.nombre) + "-" + str(aux.lleno)
            + "-" + str(aux.vacio))
            
            aux=aux.siguiente
            if aux==self.primero:
                break
            
    def NOMBRES(self):
        #FUNCION PARA OBTENER DATOS DEL
        #COMBOBOX DE LA INTERFAZ
        opciones=[]
        aux=self.primero
        while aux:
            opciones.append(aux.nombre)
            aux=aux.siguiente
            if aux==self.primero:
                break
        return opciones

    def Cantidad_nodos(self):
        contador=0
        tmp=self.primero
        while tmp:
            tmp=tmp.siguiente
            contador+=1
            if tmp==self.primero:
                break
        return (print("cantidad de nodos:"+ str(contador)))


    def buscar(self,nombre):
        aux=self.primero
        while aux:
            if aux.nombre==nombre:
                print("************************")
                print("nombre:" + aux.nombre + "\nfilas:" + str(aux.filas) + "\nColumnas:" + str(aux.columnas))
                print("-----------------")
                print("MATRIZ CARGADA")
                aux.imagen.mostrarLista()
                aux.imagen.generar_img_original(aux.nombre,aux.filas,aux.columnas)
                #aux.imagen.generar_img()
                break
            aux=aux.siguiente
            if aux==self.primero:
                break

    def buscar_y_rotar_horizontal(self,nombre):
        aux=self.primero
        while aux:
            if aux.nombre==nombre:
                print("************************")
                print("nombre:" + aux.nombre + "\nfilas:" + str(aux.filas) + "\nColumnas:" + str(aux.columnas))
                print("-----------------")
                print("MATRIZ ROTADA")
                aux.imagen.mostrarLista_Horizontal()
                aux.imagen.generar_img_horizontal(aux.nombre,aux.filas,aux.columnas)
                break
            aux=aux.siguiente
            if aux==self.primero:
                break

    def buscar_y_rotar_vertical(self,nombre):
        aux=self.primero
        while aux:
            if aux.nombre==nombre:
                print("************************")
                print("nombre:" + aux.nombre + "\nfilas:" + str(aux.filas) + "\nColumnas:" + str(aux.columnas))
                print("-----------------")
                print("MATRIZ ROTADA")
                aux.imagen.mostrarLista_Vertical()
                aux.imagen.generar_img_vertical(aux.nombre,aux.filas,aux.columnas)
                break
            aux=aux.siguiente
            if aux==self.primero:
                break

    def buscar_transpuesta(self,nombre):
        aux=self.primero
        while aux:
            if aux.nombre==nombre:
                print("************************")
                print("nombre:" + aux.nombre + "\nfilas:" + str(aux.filas) + "\nColumnas:" + str(aux.columnas))
                print("-----------------")
                print("MATRIZ ROTADA")
                if aux.filas==aux.columnas:
                    aux.imagen.mostrarLista_Transpuesta()
                    aux.imagen.generar_img_transpuesta(aux.nombre,aux.filas,aux.columnas)
                    return True
                else:
                    return False
                break
            aux=aux.siguiente
            if aux==self.primero:
                break

    def buscar_y_limpiar(self,nombre,xo,yo,x,y):
        aux=self.primero
        while aux:
            if aux.nombre==nombre:
                print("************************")
                print("nombre:" + aux.nombre + "\nfilas:" + str(aux.filas) + "\nColumnas:" + str(aux.columnas))
                print("-----------------")
                print("MATRIZ LIMPIADA")
                if aux.imagen.limpiar_zona(xo,yo,x,y)==True:
                    aux.imagen.limpiar_zona(xo,yo,x,y)
                    aux.imagen.generar_img_Aaux(aux.nombre,aux.filas,aux.columnas)
                    aux.imagen.mostrarLista()
        
                    return True
                else:
                    return False
                #aux.imagen.generar_img()
                break
            aux=aux.siguiente
            if aux==self.primero:
                break

    def buscar_e_insertar_lh(self,nombre,xo,yo,no):
        aux=self.primero
        while aux:
            if aux.nombre==nombre:
                print("************************")
                print("nombre:" + aux.nombre + "\nfilas:" + str(aux.filas) + "\nColumnas:" + str(aux.columnas))
                print("-----------------")
                print("MATRIZ LIMPIADA")
                if aux.imagen.agregarLineaHorizontal(xo,yo,no)==True:
                    aux.imagen.agregarLineaHorizontal(xo,yo,no)
                    aux.imagen.generar_img_Aaux(aux.nombre,aux.filas,aux.columnas)
                    aux.imagen.mostrarLista()

                    return True
                else:
                    return False
                #aux.imagen.generar_img()
                break
            aux=aux.siguiente
            if aux==self.primero:
                break

    def buscar_e_insertar_lv(self,nombre,xo,yo,no):
        aux=self.primero
        while aux:
            if aux.nombre==nombre:
                print("************************")
                print("nombre:" + aux.nombre + "\nfilas:" + str(aux.filas) + "\nColumnas:" + str(aux.columnas))
                print("-----------------")
                print("MATRIZ LIMPIADA")
                if aux.imagen.agregarLineaVertical(xo,yo,no)==True:
                    aux.imagen.agregarLineaVertical(xo,yo,no)
                    aux.imagen.generar_img_Aaux(aux.nombre,aux.filas,aux.columnas)
                    aux.imagen.mostrarLista()
                    return True
                else:
                    return False
                #aux.imagen.generar_img()
                break
            aux=aux.siguiente
            if aux==self.primero:
                break
    
    def buscar_e_insertar_R(self,nombre,xo,yo,alto,ancho):
        aux=self.primero
        while aux:
            if aux.nombre==nombre:
                print("************************")
                print("nombre:" + aux.nombre + "\nfilas:" + str(aux.filas) + "\nColumnas:" + str(aux.columnas))
                print("-----------------")
                print("MATRIZ LIMPIADA")
                if aux.imagen.agregar_rectangulo(xo,yo,alto,ancho)==True:
                    aux.imagen.agregar_rectangulo(xo,yo,alto,ancho)
                    aux.imagen.generar_img_Aaux(aux.nombre,aux.filas,aux.columnas)
                    aux.imagen.mostrarLista()
                    return True
                else:
                    return False
                #aux.imagen.generar_img()
                break
            aux=aux.siguiente
            if aux==self.primero:
                break
    
    def buscar_e_insertar_TR(self,nombre,xo,yo,lado):
        aux=self.primero
        while aux:
            if aux.nombre==nombre:
                print("************************")
                print("nombre:" + aux.nombre + "\nfilas:" + str(aux.filas) + "\nColumnas:" + str(aux.columnas))
                print("-----------------")
                print("MATRIZ LIMPIADA")
                if  aux.imagen.agregar_triangulo(xo,yo,lado)==True:
                    aux.imagen.agregar_triangulo(xo,yo,lado)
                    aux.imagen.generar_img_Aaux(aux.nombre,aux.filas,aux.columnas)
                    aux.imagen.mostrarLista()
                    return True
                else:
                    return False
                #aux.imagen.generar_img()
                break
            aux=aux.siguiente
            if aux==self.primero:
                break

    def CREAR_REPO_REGISTRO(self):
        os.system('cls')
        
        print ("")
        f = open('REGISTRO.html','w', encoding="utf-8")
        f.write(""" <!DOCTYPE html>
        <html lang="en">

        <head>

        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <meta name="description" content="">
        <meta name="author" content="">

        <title>PROYECTO2_IPC2</title>

        <link href="assets/img/icon.png" rel="icon">
        <link href="assets/img/apple-touch-icon.png" rel="apple-touch-icon">
        <!-- Bootstrap core CSS -->
        <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">

        <link href="img/icon.png" rel="icon">
        <link href="img/apple-touch-icon.png" rel="apple-touch-icon">

        <!-- Custom fonts for this template -->
        <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
        <link href='https://fonts.googleapis.com/css?family=Lora:400,700,400italic,700italic' rel='stylesheet' type='text/css'>
        <link href='https://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,400,300,600,700,800' rel='stylesheet' type='text/css'>

        <!-- Custom styles for this template -->
        <link href="css/clean-blog.min.css" rel="stylesheet">

        </head>

        <body>

        <!-- Navigation -->
        <nav class="navbar navbar-expand-lg navbar-light fixed-top" id="mainNav">
        <div class="container">
        <a class="navbar-brand" href="REGISTRO.html">""")
        f.write("FACULTAD DE INGENERÍA")
        f.write("""</a>
        <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
            Menu
            <i class="fas fa-bars"></i>
        </button>
        <div class="collapse navbar-collapse" id="navbarResponsive">
            <ul class="navbar-nav ml-auto">
            <li class="nav-item">
                <a class="nav-link" href="REGISTRO.html">REGISTRO</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="OPERACIONES.html">OPERACIONES</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="ERRORES.html">ERRORES</a>
            </li>
            
            </ul>
        </div>
        </div>
        </nav>

        <!-- Page Header -->
        <header class="masthead" style="background-image: url('img/R.jpg')">
        <div class="overlay"></div>
        <div class="container">
        <div class="row">
            <div class="col-lg-8 col-md-10 mx-auto">
            <div class="site-heading">
                <h1>MATRICES</h1>
                <span class="subheading">CARGADAS</span>
            </div>
            </div>
        </div>
        </div>
        </header>

        <!-- Main Content -->
        <div class="container">
        <div class="row">
        <div class="col-lg-8 col-md-10 mx-auto">
            <div class="post-preview">
            <a >
                <h2 class="post-title">
                DATOS DE MATRICES
                </h2>
                <h3 class="post-subtitle">
                
                </h3>
            </a>
            </div>
        
        <table class="table table-dark table-hover">
            <td><center><h4>NO.</h4></center></td>
            <td><center><h4>FECHA</h4></center></td>
            <td><center><h4>NOMBRE</h4></center></td>
            <td><center><h4>NO. ESPACIOS LLENOS</h4></center></td>
            <td><center><h4>NO. ESPACIOS VACÍOS</h4></center></td>
        """)
        
        aux=self.primero
        j=0
        while aux:
            j+=1
            f.write("<tr>")
            f.write("<td><center>"+"<h4>"+str(j)+"</h4>"+"</center></td>"
            +"<td>"+"<h5>"+str(aux.hora)+"</h5>"+"</td>"
            +"<td>"+"<h5>"+str(aux.nombre)+"</h5>"+"</td>"
            +"<td><center>"+"<h5>"+str(aux.lleno)+"</h5>"
            +"</center></td>"+"<td><center>"+"<h5>"+str(aux.vacio)+"</h5>"+"</center></td>"
            )     
            f.write("<t/r>")
            aux=aux.siguiente
            if aux==self.primero:
                break
        f.write("</table>")
        
        
        f.write(""" 
                    
                    <hr>

                </div>
                </div>
            </div>

            <hr>

            <!-- Footer -->
            <footer>
                <div class="container">
                <div class="row">
                    <div class="col-lg-8 col-md-10 mx-auto">
                    <ul class="list-inline text-center">
                        <li class="list-inline-item">
                        <a href="#">
                            <span class="fa-stack fa-lg">
                            <i class="fas fa-circle fa-stack-2x"></i>
                            <i class="fab fa-twitter fa-stack-1x fa-inverse"></i>
                            </span>
                        </a>
                        </li>
                        <li class="list-inline-item">
                        <a href="#">
                            <span class="fa-stack fa-lg">
                            <i class="fas fa-circle fa-stack-2x"></i>
                            <i class="fab fa-facebook-f fa-stack-1x fa-inverse"></i>
                            </span>
                        </a>
                        </li>
                        <li class="list-inline-item">
                        <a href="#">
                            <span class="fa-stack fa-lg">
                            <i class="fas fa-circle fa-stack-2x"></i>
                            <i class="fab fa-github fa-stack-1x fa-inverse"></i>
                            </span>
                        </a>
                        </li>
                    </ul>
                    <p class="copyright text-muted"> &copy; Facultad de Ingenería 2021</p>
                    </div>
                </div>
                </div>
            </footer>

            <!-- Bootstrap core JavaScript -->
            <script src="vendor/jquery/jquery.min.js"></script>
            <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

            <!-- Custom scripts for this template -->
            <script src="js/clean-blog.min.js"></script>

            </body>

            </html>
        """)
        
        f.close()

    def CREAR_REPO_OPERACIONES(self):

        f = open('OPERACIONES.html','w', encoding="utf-8")
        f.write(""" <!DOCTYPE html>
            <html lang="en">

            <head>

            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <meta name="description" content="">
            <meta name="author" content="">

            <title>PROYECTO2_IPC2</title>

            <link href="assets/img/icon.png" rel="icon">
            <link href="assets/img/apple-touch-icon.png" rel="apple-touch-icon">
            <!-- Bootstrap core CSS -->
            <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">

            <link href="img/icon.png" rel="icon">
            <link href="img/apple-touch-icon.png" rel="apple-touch-icon">

            <!-- Custom fonts for this template -->
            <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
            <link href='https://fonts.googleapis.com/css?family=Lora:400,700,400italic,700italic' rel='stylesheet' type='text/css'>
            <link href='https://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,400,300,600,700,800' rel='stylesheet' type='text/css'>

            <!-- Custom styles for this template -->
            <link href="css/clean-blog.min.css" rel="stylesheet">

            </head>

            <body>

            <!-- Navigation -->
            <nav class="navbar navbar-expand-lg navbar-light fixed-top" id="mainNav">
            <div class="container">
            <a class="navbar-brand" href="REGISTRO.html">""") 
        f.write("FACULTAD DE INGENERÍA")
        f.write("""</a>
            <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
            Menu
            <i class="fas fa-bars"></i>
            </button>
            <div class="collapse navbar-collapse" id="navbarResponsive">
                <ul class="navbar-nav ml-auto">
                <li class="nav-item">
                <a class="nav-link" href="REGISTRO.html">REGISTRO</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="OPERACIONES.html">OPERACIONES</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="ERRORES.html">ERRORES</a>
            </li>
            
            </ul>
        </div>
        </div>
        </nav>

        <!-- Page Header -->
        <header class="masthead" style="background-image: url('img/r2.jpg')">
            <div class="overlay"></div>
            <div class="container">
            <div class="row">
                <div class="col-lg-8 col-md-10 mx-auto">
                <div class="site-heading">
                    <h1>OPERACIONES</h1>
                    <span class="subheading">REGISTRO DE OPERACIONES</span>
                </div>
                </div>
            </div>
            </div>
        </header>

        <!-- Main Content -->
        <div class="container">
        <div class="row">
        <div class="col-lg-8 col-md-10 mx-auto">
        """)
        
        f.write("""
        
            <div class="post-preview">
            <a>
                <h2 class="post-title">
                OPERACIONES REALIZADAS
                </h2>
            </a>
            <p class="post-meta">
                <table class="table table-dark table-hover">
                <td><center><h4>NO.</h4></center></td>
                <td><center><h4>HORA</h4></center></td>
                <td><center><h4>OPERACION</h4></center></td>
                <td><center><h4>NOMBRE</h4></center></td>
        """)
        aux=self.primero
        j=0
        while aux:
            j+=1
            f.write("<tr>")
            f.write("<td><center>"+"<h4>"+str(j)+"</h4>"+"</center></td>"
            +"<td>"+"<h5>"+str(aux.hora)+"</h5>"+"</td>"
            +"<td>"+"<h5>"+aux.operacion+"</h5>"+"</td>"
            +"<td>"+"<h5>"+str(aux.nombre)+"</h5>"+"</td>"
            )     
            f.write("<t/r>")
            aux=aux.siguiente
            if aux==self.primero:
                break
        f.write("</table>")
        f.write(""" 
                    </div>
                    <hr>

                </div>
                </div>
            </div>

            <hr>

            <!-- Footer -->
            <footer>
                <div class="container">
                <div class="row">
                    <div class="col-lg-8 col-md-10 mx-auto">
                    <ul class="list-inline text-center">
                        <li class="list-inline-item">
                        <a href="#">
                            <span class="fa-stack fa-lg">
                            <i class="fas fa-circle fa-stack-2x"></i>
                            <i class="fab fa-twitter fa-stack-1x fa-inverse"></i>
                            </span>
                        </a>
                        </li>
                        <li class="list-inline-item">
                        <a href="#">
                            <span class="fa-stack fa-lg">
                            <i class="fas fa-circle fa-stack-2x"></i>
                            <i class="fab fa-facebook-f fa-stack-1x fa-inverse"></i>
                            </span>
                        </a>
                        </li>
                        <li class="list-inline-item">
                        <a href="#">
                            <span class="fa-stack fa-lg">
                            <i class="fas fa-circle fa-stack-2x"></i>
                            <i class="fab fa-github fa-stack-1x fa-inverse"></i>
                            </span>
                        </a>
                        </li>
                    </ul>
                    <p class="copyright text-muted"> &copy; Facultad de Ingenería 2021</p>
                    </div>
                </div>
                </div>
            </footer>

            <!-- Bootstrap core JavaScript -->
            <script src="vendor/jquery/jquery.min.js"></script>
            <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

            <!-- Custom scripts for this template -->
            <script src="js/clean-blog.min.js"></script>

            </body>

            </html>
        """)
        f.close()   

    def CREAR_REPO_ERRORES(self):

        f = open('ERRORES.html','w', encoding="utf-8")
        f.write(""" <!DOCTYPE html>
            <html lang="en">

            <head>

            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <meta name="description" content="">
            <meta name="author" content="">

            <title>PROYECTO2_IPC2</title>

            <link href="assets/img/icon.png" rel="icon">
            <link href="assets/img/apple-touch-icon.png" rel="apple-touch-icon">
            <!-- Bootstrap core CSS -->
            <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">

            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BmbxuPwQa2lc/FVzBcNJ7UAyJxM6wuqIj61tLrc4wSX0szH/Ev+nYRRuWlolflfl" crossorigin="anonymous">

            <link href="img/icon.png" rel="icon">
            <link href="img/apple-touch-icon.png" rel="apple-touch-icon">

            <!-- Custom fonts for this template -->
            <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
            <link href='https://fonts.googleapis.com/css?family=Lora:400,700,400italic,700italic' rel='stylesheet' type='text/css'>
            <link href='https://fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,400,300,600,700,800' rel='stylesheet' type='text/css'>

            <!-- Custom styles for this template -->
            <link href="css/clean-blog.min.css" rel="stylesheet">

            </head>

            <body>

            <!-- Navigation -->
            <nav class="navbar navbar-expand-lg navbar-light fixed-top" id="mainNav">
            <div class="container">
            <a class="navbar-brand" href="REGISTRO.html">""") 
        f.write("FACULTAD DE INGENERÍA")
        f.write("""</a>
            <button class="navbar-toggler navbar-toggler-right" type="button" data-toggle="collapse" data-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
            Menu
            <i class="fas fa-bars"></i>
            </button>
            <div class="collapse navbar-collapse" id="navbarResponsive">
                <ul class="navbar-nav ml-auto">
                <li class="nav-item">
                <a class="nav-link" href="REGISTRO.html">REGISTRO</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="OPERACIONES.html">OPERACIONES</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="ERRORES.html">ERRORES</a>
            </li>
            
            </ul>
        </div>
        </div>
        </nav>

        <!-- Page Header -->
        <header class="masthead" style="background-image: url('img/r2.jpg')">
            <div class="overlay"></div>
            <div class="container">
            <div class="row">
                <div class="col-lg-8 col-md-10 mx-auto">
                <div class="site-heading">
                    <h1>ERRORES</h1>
                    <span class="subheading">REGISTRO DE ERRORES</span>
                </div>
                </div>
            </div>
            </div>
        </header>

        <!-- Main Content -->
        <div class="container">
        <div class="row">
        <div class="col-lg-8 col-md-10 mx-auto">
        """)
        
        f.write("""
        
            <div class="post-preview">
            <a>
                <h2 class="post-title">
                ERRORES REGISTRADOS
                </h2>
            </a>
            <p class="post-meta">
                <table class="table table-dark table-hover">
                <td><center><h4>NO.</h4></center></td>
                <td><center><h4>HORA</h4></center></td>
                <td><center><h4>DESCRIPCIÓN</h4></center></td>
                
        """)
        aux=self.primero
        j=0
        while aux:
            j+=1
            f.write("<tr>")
            f.write("<td><center>"+"<h4>"+str(j)+"</h4>"+"</center></td>"
            +"<td>"+"<h5>"+str(aux.hora)+"</h5>"+"</td>"
            +"<td>"+"<h5>"+str(aux.descripcion)+"</h5>"+"</td>"
            )     
            f.write("<t/r>")
            aux=aux.siguiente
            if aux==self.primero:
                break
        f.write("</table>")
        f.write(""" 
                    </div>
                    <hr>

                </div>
                </div>
            </div>

            <hr>

            <!-- Footer -->
            <footer>
                <div class="container">
                <div class="row">
                    <div class="col-lg-8 col-md-10 mx-auto">
                    <ul class="list-inline text-center">
                        <li class="list-inline-item">
                        <a href="#">
                            <span class="fa-stack fa-lg">
                            <i class="fas fa-circle fa-stack-2x"></i>
                            <i class="fab fa-twitter fa-stack-1x fa-inverse"></i>
                            </span>
                        </a>
                        </li>
                        <li class="list-inline-item">
                        <a href="#">
                            <span class="fa-stack fa-lg">
                            <i class="fas fa-circle fa-stack-2x"></i>
                            <i class="fab fa-facebook-f fa-stack-1x fa-inverse"></i>
                            </span>
                        </a>
                        </li>
                        <li class="list-inline-item">
                        <a href="#">
                            <span class="fa-stack fa-lg">
                            <i class="fas fa-circle fa-stack-2x"></i>
                            <i class="fab fa-github fa-stack-1x fa-inverse"></i>
                            </span>
                        </a>
                        </li>
                    </ul>
                    <p class="copyright text-muted"> &copy; Facultad de Ingenería 2021</p>
                    </div>
                </div>
                </div>
            </footer>

            <!-- Bootstrap core JavaScript -->
            <script src="vendor/jquery/jquery.min.js"></script>
            <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

            <!-- Custom scripts for this template -->
            <script src="js/clean-blog.min.js"></script>

            </body>

            </html>
        """)
        f.close()   

    def recorrer_OP(self):
        aux=self.primero
        while aux:
            print("************************")
            print(str(aux.hora) + "-" + str(aux.operacion) + "-" + str(aux.nombre))
            aux=aux.siguiente
            if aux==self.primero:
                break
    def recorrer_ER(self):
        aux=self.primero
        while aux:
            print("************************")
            print(str(aux.hora) + "-" + str(aux.descripcion))
            aux=aux.siguiente
            if aux==self.primero:
                break
  


