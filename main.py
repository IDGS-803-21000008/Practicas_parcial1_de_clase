from flask import Flask, render_template, request, redirect
import forms
import math
import resistencias
app = Flask(__name__)

@app.route("/formulario1")
def formulario1():
    return render_template("formulario1.html")

@app.route("/resultado", methods=["GET", "POST"])
def mult():
    if request.method == "POST":
        num1=request.form.get("n1")
        num2=request.form.get("n2")
        operacion = request.form.get("operacion")

    # Realizar la operación correspondiente
        if operacion == 'suma':
            resultado = int(num1) + int(num2)
        elif operacion == 'resta':
            resultado =  int(num1) - int(num2)
        elif operacion == 'multiplicacion':
            resultado = int(num1) * int(num2)
        elif operacion == 'division':
            if num2 != 0:
                resultado = int(num1) / int(num2)
            else:
                resultado = 'Error: División por cero'
                
        return "<h1>El resultado es: {}</h1>".format(str(resultado))
    
@app.route("/calcular", methods=["GET", "POST"])
def calcularValorAPagar(): #preguntar si la cantidad de compradores influye en la cantidad de boletos
    resultado = "Error, no se ha calculado el precio"
    #render_template("vista_cine.html", resultado = "", nombre = "")
    if request.method == "POST":
        nombre = request.form.get("nombre")
        cantidadCompradores = int(request.form.get("cantidad_compradores"))
        tarjeta = request.form.get("tarjeta")
        cantidadBoletos = int(request.form.get("cantidad_boletos"))
        
        cantidadMax = cantidadCompradores * 7

        if cantidadBoletos > cantidadMax:
            resultado = "Error, no se pueden vender más de 7 boletos por persona"
        else:
            if cantidadBoletos > 5:
                precioFinal = (cantidadBoletos * 12)
                precioFinal = precioFinal - (precioFinal*0.15)
            elif 3 <= cantidadBoletos <= 5:
                precioFinal = (cantidadBoletos * 12)
                precioFinal = precioFinal - (precioFinal*0.10)
            else:
                precioFinal = cantidadBoletos * 12

            if tarjeta == "si":
               # precioFinal *= 1.10
                precioFinal = precioFinal - (precioFinal*0.10)
            
            resultado = str(precioFinal)
            
    return render_template("vista_cine.html",
                           resultado=resultado,
                           nombre=nombre,
                           cantidadBoletos = str(cantidadBoletos),
                           cantidadCompradores = str(cantidadCompradores),
                           tarjeta = tarjeta)
   #return "<h1>El resultado es: {}</h1>".format(str(resultado))


@app.route("/home", methods=["GET", "POST"])
def cinepolis():
    return render_template("vista_cine.html",
                           resultado="",
                           nombre="",
                           cantidadBoletos = "",
                           cantidadCompradores = "",
                           tarjeta = "")

@app.route("/distancia",methods=["GET","POST"])
def calcularDistancia():
    dist_form = forms.distancia(request.form)
    resultado = 0.0
    if request.method == "POST":
        
        x1 = dist_form.x1.data
        x2 = dist_form.x2.data
        y1 = dist_form.y1.data
        y2 = dist_form.y2.data
        resultado1 = math.pow((x2-x1),2)
        resultado2 = math.pow((y2-y1),2)
        resultado = math.sqrt(resultado1 + resultado2)
        print(resultado)
        
    
    return render_template("distancia.html", form = dist_form, resultado = resultado )

@app.route("/resistencia", methods=["GET", "POST"])
def calcularResistencia():
    if request.method == "GET":
        res_form = resistencias.resistencia(request.form)
        return render_template("resistencias.html", form= res_form, valorMaximo = 0, valor = 0,  valorMinimo = 0)
    else:
        res_form = resistencias.resistencia(request.form)
        resultado = 0
        banda1 = res_form.primeraBanda.data
        banda2 = res_form.segundaBanda.data
        banda3 = res_form.terceraBanda.data
        tolerancia = res_form.tolerancia.data
        v1 = 0
        v2 = 0
        v3 = 0
        valTolerancia = 0
        
        #variables para los colores
        negro = 0
        cafe = 1
        rojo = 2
        naranja = 3
        amarillo = 4
        verde = 5
        azul = 6
        violeta = 7
        gris = 8
        blanco = 9
        
        negroMul = 1
        cafeMul = 10
        rojoMul = 100
        naranjaMul = 1000
        amarilloMul = 10000
        verdeMul = 100000
        azulMul = 1000000
        violetaMul = 10000000
        grisMul = 100000000
        blancoMul = 1000000000
        
        negroCol = "#000000"
        cafeCol = "#8B4513 "
        rojoCol = "#FF0000"
        naranjaCol = "#FFA500"
        amarilloCol = "#FFFF00"
        verdeCol = "#008000"
        azulCol = "#0000FF"
        violetaCol = "#EE82EE"
        grisCol = "#808080"
        blancoCol = "#FFFFFF"
        colTol = "#C0C0C0"
        
        
        if banda1 == "negro":
            v1 = negro
            color = negroCol
        elif banda1 == "cafe":
            v1 = cafe
            color = cafeCol
        elif banda1 == "rojo":
            v1 = rojo
            color = rojoCol
        elif banda1 == "naranja":
            v1 = naranja
            color = naranjaCol
        elif banda1 == "amarillo":
            v1 = amarillo
            color = amarilloCol
        elif banda1 == "verde":
            v1 = verde
            color = verdeCol
        elif banda1 == "azul":
            v1 = azul
            color = azulCol
        elif banda1 == "violeta":
            v1 = violeta
            color = violetaCol
        elif banda1 == "gris":
            v1 = gris
            color = grisCol
        elif banda1 == "blanco":
            v1 = blanco
            color = blancoCol
            
        if banda2 == "negro":
            v2 = negro
            color2 = negroCol
        elif banda2 == "cafe":
            v2 = cafe
            color2 = cafeCol
        elif banda2 == "rojo":
            v2 = rojo
            color2 = rojoCol
        elif banda2 == "naranja":
            v2 = naranja
            color2 = naranjaCol
        elif banda2 == "amarillo":
            v2 = amarillo
            color2 = amarilloCol
        elif banda2 == "verde":
            v2 = verde
            color2 = verdeCol
        elif banda2 == "azul":
            v2 = azul
            color2 = azulCol
        elif banda2 == "violeta":
            v2 = violeta
            color2 = violetaCol
        elif banda2 == "gris":
            v2 = gris
            color2 = grisCol
        elif banda2 == "blanco":
            v2 = blanco
            color2 = blancoCol
        
        if banda3 == "negro":
            v3 = negroMul
            color3 = negroCol
        elif banda3 == "cafe":
            v3 = cafeMul
            color3 = cafeCol
        elif banda3 == "rojo":
            v3 = rojoMul
            color3 = rojoCol
        elif banda3 == "naranja":
            v3 = naranjaMul
            color3 = naranjaCol
        elif banda3 == "amarillo":
            v3 = amarilloMul
            color3 = amarilloCol
        elif banda3 == "verde":
            v3 = verdeMul
            color3 = verdeCol
        elif banda3 == "azul":
            v3 = azulMul
            color3 = azulCol
        elif banda3 == "violeta":
            v3 = violetaMul
            color3 = violetaCol
        elif banda3 == "gris":
            v3 = grisMul
            color3 = grisCol
        elif banda3 == "blanco":
            v3 = blancoMul
            color3 = blancoCol
            
        if tolerancia == "oro":
            valTolerancia = 0.05
            colTol = "#FFD700"
        elif tolerancia == "plata":
            valTolerancia = 0.10
            colTol = "#C0C0C0"
            
        cadenaControl = str(v1) + str(v2)
        
        valorFinal = int(cadenaControl)
        
        resultado = valorFinal * v3 #valor
        
        valorMaximo = resultado + (resultado * valTolerancia) #Valor maximo
        
        valorMinimo = resultado - (resultado * valTolerancia)
        
        
            
    
        
        return render_template("resistencias.html", form= res_form, valorMaximo = valorMaximo, valor = resultado, valorMinimo = valorMinimo,color= color, color2 = color2, color3= color3, colTol = colTol)


if __name__ == "__main__":
    app.run(debug=True)