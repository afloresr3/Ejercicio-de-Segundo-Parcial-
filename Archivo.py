class archivo:
    def __init__(self,nombreArchivo,separador=''):
        self.__archivo = nombreArchivo
        self.__separ = separador
        
    def leer(self):
        with open(self.__archivo,'r',encodig="UTF-8") as file:
            lista=[]
            for linea in file:
                lista.append(linea[:-1])
        return lista        
            
            
    def escribir(self,datos,modo,):
        with open(self.__archivo, modo, encoding="UTF-8") as file:
            for dato in datos:
                file.write(dato+'\n')
    
    def escribirE(self,datos,modo):
        with open(self.__archivo, modo, encoding="UTF-8") as file:
            for dato in datos:
                linea=''
                for valor in dato:
                    if type(valor) == int or float: linea +=str(valor)+self.__separ
                    else: linea += valor + self.__separ
                    file.write(linea[:-1]+'\n')           

articulo = [[1,"aceite","girazol",2.50,100],[1,"aceite","girazol",2.50,100],[1,"aceite","girazol",2.50,100]]        
arch = archivo("estudiantes.txt",":")
arch.escribirE(articulo,"a")
# lista = arch.leer()
# print(lista)          