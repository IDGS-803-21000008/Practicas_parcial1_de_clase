class Ejercicio1:
    #Propiedades
    num = 0
    x = 0
    #Constructor
    def __init__(self,a):
        self.num = a
        
    #Metodos

    def hacer_piramide2(self):
        i=0
        while i < self.num:
            j = 0
            while j <= i:
                print("*", end = "")
                j += 1
            print()
            i += 1
                

def main():
    tamanio_piramide = int(input("Dame el tamaño de la piramide: "))
    obj = Ejercicio1(tamanio_piramide)
    obj.hacer_piramide2()
    
if __name__ == "__main__":
    main()