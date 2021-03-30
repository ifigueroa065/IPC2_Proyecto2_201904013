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
        else:
            aux=self.cabeza
            #recorrido vertical
            while aux.bot!=None:
                aux=aux.bot
            if lista_Ortogonal.cont !=fila:
                lista_Ortogonal.cont+=1
                tempNodo=NODO(pix)
                aux.bot=tempNodo    #apunta abajo
                tempNodo.top=aux    #apunta arriba    
            else: 
                #recorrido horizontal
                while aux.right!=None:
                    aux=aux.right
                tempNodo=NODO(pix)
                aux.right=tempNodo
                tempNodo.left=aux
                if lista_Ortogonal.cont>1:
                    #creando 2do nodo auxiliar
                    aux2=aux.top.right
                    aux2.bot=tempNodo
                    tempNodo.top=aux2
    
    def mostrarLista(self):
        aux=self.cabeza
        img=""
        while aux.bot !=None or aux.right!=None:
            img+=aux.pix
            if aux.right !=None:
                aux=aux.right
            else:
                print(img)
                if aux.bot!=None:
                    img=""
                    aux=aux.bot
                    while aux.left!=None:
                        aux=aux.left
        img+=aux.pix
        print(img)
prueba=lista_Ortogonal()

prueba.agregarNodo("*",1)
prueba.agregarNodo("-",1)
prueba.agregarNodo("*",1)
prueba.agregarNodo("-",1)

prueba.agregarNodo("*",2)
prueba.agregarNodo("-",2)
prueba.agregarNodo("-",2)
prueba.agregarNodo("*",2)

prueba.mostrarLista()

            