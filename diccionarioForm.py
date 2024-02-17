from wtforms import Form
from wtforms import StringField, SelectField, RadioField, EmailField, IntegerField
from wtforms import validators
from wtforms.validators import DataRequired

class Traductor(Form):
    ingles = StringField('ingles', [
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=4, max=15, message='ingresa una palabra valida')
    ])
    espaniol = StringField('espaniol',[
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=4, max=15, message='ingresa una palabra valida')
    ])
   
    




class buscar(Form):
    campoABuscar = StringField('campoABuscar',[
        validators.DataRequired(message='el campo es requerido'),
        validators.length(min=4, max=15, message='ingresa una palabra valida')
    ])
    radioIdioma = RadioField('Idioma', 
                         choices=[('ingles', 'Inglés'), ('espaniol', 'Español')],
                         validators=[DataRequired(message="Este campo es obligatorio.")])
    
    