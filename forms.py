from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, FloatField, IntegerField
from wtforms.validators import Required, Length, ValidationError

#Validaciones Custom
def validarCodigo(form, campo):
    cont = 1
    for caracter in campo.data:
        if cont < 4:
            if caracter.isdigit():
                raise ValidationError('El campo "codigo" debe tener letras en los primeros 3 caracteres seguido de 3 dígitos.')
        else:
            if caracter.isdigit() == False:
                raise ValidationError('El campo "codigo" debe tener letras en los primeros 3 caracteres seguido de 3 dígitos.')
        cont += 1

#Clase para crear el formulario de la busqueda del Cliente, donde sus validaciones seran que es "requerido" y que tenga "minimo 3 caracteres"
class ClienteForm(FlaskForm):
    cliente = StringField('Ingresar Cliente: ', validators=[Required(), Length(min=3, message="Ingresa minimo 3 caracteres.")])
    buscar = SubmitField('Buscar')

#Clase para crear el formulario de la busqueda del Producto, donde sus validaciones seran que es "requerido" y que tenga "minimo 3 caracteres"
class ProductoForm(FlaskForm):
    producto = StringField('Ingresar Producto: ', validators=[Required(), Length(min=3,message="Ingresa minimo 3 caracteres.")])
    buscar = SubmitField('Buscar')

#Clase para crear el formulario que permite el ingreso de datos, donde cada campo tiene su validación correspondiente.
class ingresarDatosForm(FlaskForm):
    cliente = StringField('Ingresar Cliente: ', validators=[Required()])
    producto = StringField('Ingresar Producto: ', validators=[Required()])
    cantidad = IntegerField('Ingresar Cantidad: ', validators=[Required("Ingresar números enteros.")])
    precio =  FloatField('Ingresar Precio: ', validators=[Required("Ingresar números decimales.")])
    codigo = StringField('Ingresar Codigo: ', validators=[Required(), validarCodigo, Length(min=6, max=6, message="Se debe ingresar 6 caracteres obligatoriamente.")])
    agregar = SubmitField('Agregar')