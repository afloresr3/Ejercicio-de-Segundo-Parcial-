class Pila:
    def __init__(self,tamanio):
        self.__lista = []
        self.__tope = 0
        self.__size = tamanio
        
    def empty(self):
        return self.__tope == 0
        # if self.__tope == 0:
        #     return True
        # else:
        #     return False 

    def push(self,dato):
        if self.__tope < self.__size:
            self.__lista = self.__lista + [dato]
            self.__tope += 1
        else:
            print("la lista esta llena")
        # esto es equivalente a appent   
    
    def pop(self):
        if self.empty():
            return None
        else:
            top = self.__lista[-1]
            self.__tope -= 1
            self.__lista = self.__lista[:-1]            
            return top
    
    def show(self):
        for top in range(self.__tope-1,-1,-1):    
            print("[{}]".format(self.__lista[top]))
            
            
