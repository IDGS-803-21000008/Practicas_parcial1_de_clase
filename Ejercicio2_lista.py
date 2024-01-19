class Ejercicio2:
    #Propiedades
    numero_datos = 0
    numeros_pares = set()
    numeros_impares = set()
    conteo = 0
    numero_a_revisar = 0
    numeros_procesados = set() #La funcion set no permite elementos duplicados, es un conjunto
    
    #Constructor
    def __init__(self,a):
        self.numero_datos = a
        
    #Metodos
    def hacer_proceso(self):
        lista_sin_ordenar = []
        for num in range(self.numero_datos):
            numero_ingresado = int(input(f"ingresa el numero {num + 1}: "))
            lista_sin_ordenar.append(numero_ingresado)
        print(f"Tu lista sin ordenar es: {lista_sin_ordenar}")
        lista_ordenada = sorted(lista_sin_ordenar)
        print(f'Tu lista ordenada es: {lista_ordenada}')
        
        num_elementos = lista_ordenada.__len__()
        for num2 in range(num_elementos):
            if(lista_ordenada[num2] % 2 == 0):
                self.numeros_pares.add(lista_ordenada[num2])
            else:
                self.numeros_impares.add(lista_ordenada[num2])
        
        print(f'Los números pares son: {self.numeros_pares}')
        print(f'Los números impares son: {self.numeros_impares}')

        for num3 in range(len(lista_ordenada)):
            numero_a_revisar = lista_ordenada[num3]
            if numero_a_revisar in self.numeros_procesados:
                continue #Se usa la palabra continue para no seguir con el resto del bloque de código
            conteo = lista_ordenada.count(numero_a_revisar)
            if conteo > 1:
                print(f'El número {numero_a_revisar} aparece {conteo} veces')
            self.numeros_procesados.add(numero_a_revisar)#Se agrega a numeros procesados para hacer la comparacion anterior
            

def main():
    numero_items = int(input("Dame el tamaño de la lista: "))
    obj = Ejercicio2(numero_items)
    obj.hacer_proceso()
    
if __name__ == "__main__":
    main()