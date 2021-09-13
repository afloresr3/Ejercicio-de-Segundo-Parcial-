import os
class Matriz:
    def __init__(self,nfilas,ncol):
        self.matriz = []
        self.nfilas = nfilas
        self.ncol = ncol
        
    def ingresar(self):
        self.matriz = []
        for fila in range(self.nfilas):
            columnas = []
            for col in range(self.ncol):
                valor = int(input("Fila[{}] col[{}]:".format(fila,col)))
                columnas.append(valor)
            self.matriz.append(columnas) 
            
    def mostrar(self):
        os.system("cls")
        print("--------------")
        for fila in range(len(self.matriz)):
            for col in range(len(self.matriz[fila])):
                print("[{}]".format(self.matriz[fila][col]),end=" ")
            print()
        print("--------------")
    
    def buscar(self,buscado):
        resp= {}           
        for fila in range(len(self.matriz)):
            for col in range(len(self.matriz[fila])):
                if self.matriz[fila][col] == buscado:
                    resp["fila"]=fila
                    resp["col"]=col
                    break
            if resp: break      
        return resp
    
    def buscarE(self,buscado):
        resp= {}
        fila=0
        enc=False           
        while fila < len(self.matriz) and enc==False:
            col=0
            while col < len(self.matriz) and enc==False:
                if self.matriz[fila][col] == buscado:
                    resp["fila"]=fila
                    resp["col"]=col
                    enc=True
                else: col +=1
            fila +=1    
        return resp
    
    def sumar(self,mat2):
        matrizSuma = []
        for fila in range(self.nfilas):
            columnas = []
            for col in range(self.ncol):
                valor = self.matriz[fila][col] + mat2[fila][col]
                columnas.append(valor)
            matrizSuma.append(columnas)
        print(matrizSuma)        
        
            
numero = []
mat = Matriz(2,2)
mat.ingresar()
mat2 = Matriz(2,2)
mat2.ingresar()
mat.mostrar()
mat2.mostrar()
mat.sumar(mat2.matriz)
#if mat.buscarE(25): print(mat.buscar(25))
#else:print("dato no encontrado")            