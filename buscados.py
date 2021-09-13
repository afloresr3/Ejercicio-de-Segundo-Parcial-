class buscado:
    def __init__(self,listas=None):
        self.__lista = listas
    
    # retorna el valor de un atributo
    @property
    def lista(self):
        if self.__lista != None:   
            return self.__lista
        else: print("lista vacia")
    # @lista.setter
    # def lista(self,valor): cambia el valor de un atributo
    #     self.__lista=valor
                
    def busquedaLineal(self,buscado):
        lon = len(self.lista)
        enc=False
        pos=0
        while pos < lon and enc==False:
            if self.__lista[pos] == buscado: enc=True
            else: pos +=1
        if enc: return pos 
        else: return -1 
          
    def ordenar(self,orden):
        if orden =="asc":
            for pos in range(0,len(self.__lista)):
                for sig in range(pos+1,len(self.__lista)):
                    if self.__lista[pos]["nombre"] > self.__lista[sig]["nombre"]:
                        aux = self.__lista[pos]
                        self.__lista[pos]=self.__lista[sig]
                        self.__lista[sig]=aux
        else:
            for pos in range(0,len(self.__lista)):
                for sig in range(pos+1,len(self.__lista)):
                    if self.__lista[pos]["nombre"] < self.__lista[sig]["nombre"]:
                        aux = self.__lista[pos]
                        self.__lista[pos]=self.__lista[sig]
                        self.__lista[sig]=aux 
                                       
    def busquedaBinaria(self,buscado):
        self.ordenar("asc")
        fin = len(self.lista)-1
        inicio = 0
        enc = False
        while inicio <= fin and enc==False:
            medio =(inicio+fin)//2
            if self.lista[medio]["nombre"] == buscado: enc= True
            elif self.lista[medio]["nombre"] < buscado: inicio = medio+1
            else: fin = medio-1
        if enc: return medio
        else: return -1    

nota = [
    {"nombre":"daniel","n1":20,"n2":40},
    {"nombre":"dayana","n1":30,"n2":50},
    {"nombre":"erick","n1":40,"n2":50},
    {"nombre":"romina","n1":50,"n2":40},
    {"nombre":"Yady","n1":55,"n2":40},
    {"nombre":"Eddy","n1":60,"n2":60}
]

bus1 = buscado(nota)
print(bus1.busquedaBinaria("Eddy"))
#print(bus1.busquedaLineal("Eddy"))
# bus1.ordenar("asc")
# print(bus1.lista)
# bus2 = buscado(["Ana","Dan","Abdon"])
# print("bus2",bus2.lista)       