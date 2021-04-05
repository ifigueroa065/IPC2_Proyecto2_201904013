from NodoC import Nodo_C
from ORTOGONAL import lista_Ortogonal
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
                aux.imagen.mostrarLista_Horizontal()
                break
            aux=aux.siguiente
            if aux==self.primero:
                break