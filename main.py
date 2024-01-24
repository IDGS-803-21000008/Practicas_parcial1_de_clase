from flask import Flask, render_template, request

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
    
    

if __name__ == "__main__":
    app.run(debug=True)