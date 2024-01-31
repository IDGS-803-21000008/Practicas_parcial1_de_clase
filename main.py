from flask import Flask, render_template, request, redirect
import forms
import math
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


if __name__ == "__main__":
    app.run(debug=True)