class OPERACION():
    def __init__(self,hora,nombre,lleno,vacio):
        self.hora=hora
        self.nombre=nombre
        self.lleno=lleno
        self.vacio=vacio
    
class ERROR():
    def __init__(self,hora,descripcion):
        self.hora=hora
        self.descripcion=descripcion

class OP():
    def __init__(self,hora,operacion,nombre):
        self.hora=hora
        self.operacion=operacion
        self.nombre=nombre
        
