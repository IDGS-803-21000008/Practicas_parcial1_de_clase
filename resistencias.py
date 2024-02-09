from wtforms import Form
from wtforms import StringField, SelectField, RadioField, EmailField, IntegerField, FloatField, SelectField

class resistencia(Form):
    
    primeraBanda = SelectField('primeraBanda',choices=[('negro', 'negro'), ('cafe', 'cafe'), ('rojo', 'rojo'), ('naranja', 'naranja'), ('amarillo', 'amarillo') , ('verde', 'verde') , ('azul', 'azul') , ('violeta', 'violeta') , ('gris', 'gris'),('blanco', 'blanco')])
    segundaBanda = SelectField('segundaBanda',choices=[('negro', 'negro'), ('cafe', 'cafe'), ('rojo', 'rojo'), ('naranja', 'naranja'), ('amarillo', 'amarillo') , ('verde', 'verde') , ('azul', 'azul') , ('violeta', 'violeta') , ('gris', 'gris'),('blanco', 'blanco')])
    terceraBanda = SelectField('terceraBanda',choices=[('negro', 'negro'), ('cafe', 'cafe'), ('rojo', 'rojo'), ('naranja', 'naranja'), ('amarillo', 'amarillo') , ('verde', 'verde') , ('azul', 'azul') , ('violeta', 'violeta') , ('gris', 'gris'),('blanco', 'blanco')])
    tolerancia = SelectField('tolerancia',choices=[('oro', 'oro'), ('plata', 'plata')])
    