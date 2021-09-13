class Lista:
    def __init__(self,tamanio):
        self.lista = []
        self.longitud=0
        self.size = tamanio
        
    def append(self,dato):
        if self.longitud < self.size:
            self.lista += [dato]
            self.longitud += 1
        else:
            print("lista esta llena")
    
    def obtener(self,pos):
        if pos < 0 or pos >= self.longitud:
            return -1
        else:
            valor = self.lista[pos]
            self.lista = self.lista[0:pos] + self.lista[pos+1:]
            self.longitud -= 1
            return valor 
            
    def buscar(self,dato):
        ban = False
        for a in range(0,self.longitud):
            if dato == self.lista[a]:
                ban = True
                break
        if ban: return a
        else: return -1
            
    def insertar(self,dato):
        if self.buscar(dato) == -1:
            self.append(dato)
        else: print("No se insertó el dato porque ya existe en la lista")
                     
    def eliminar(self,dato):
        pos = self.buscar(dato)
        if pos != -1:
            self.lista = self.lista[0:pos] + self.lista[pos+1:] 
            self.longitud -= 1
        else: return -1                 
            
    def mostrar(self,orden="asc"):
        if orden.lower() == "asc":
            for pos in range(0,self.longitud):
                print("[{}]".format(self.lista[pos]))
        else:
            for pos in range(self.longitud-1,-1,-1):
                print("[{}]".format(self.lista[pos]))
    
              
                     
                            