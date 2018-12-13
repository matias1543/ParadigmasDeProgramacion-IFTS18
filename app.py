#!/usr/bin/env python
import csv
import funciones
from datetime import datetime
from flask import Flask, render_template, redirect, url_for, flash, session
from flask_bootstrap import Bootstrap
# from flask_moment import Moment
from flask_script import Manager
from forms import ClienteForm, ProductoForm, ingresarDatosForm

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
# moment = Moment(app)

app.config['SECRET_KEY'] = 'un string que funcione como llave'


@app.route('/')
def index():
    return render_template('index.html', fecha_actual=datetime.utcnow())

@app.errorhandler(404)
def no_encontrado(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def error_interno(e):
    return render_template('500.html'), 500


@app.route('/listacompleta')
def lista():
    datosDeVentas = funciones.lecturaDeVentas()
    if len(datosDeVentas) == 1:
        return render_template('errores/errores.html', lista=datosDeVentas)
    posicionDeCliente = funciones.posicionDelDato('CLIENTE')
    posicionDePrecio = funciones.posicionDelDato('PRECIO')
    posicionDeCantidad = funciones.posicionDelDato('CANTIDAD')
    posicionDeCodigo = funciones.posicionDelDato('CODIGO')
    validaciones = funciones.validaciones(datosDeVentas, posicionDePrecio, posicionDeCantidad, posicionDeCodigo)
    if len(validaciones):
        return render_template('errores/errores.html', lista=validaciones)
    return render_template('lista_completa.html', ventas=datosDeVentas)

@app.route('/productosxcliente', methods=['GET', 'POST'])
def formBusquedaCliente():
    formulario = ClienteForm()
    datosDeVentas = funciones.lecturaDeVentas()
    if len(datosDeVentas) == 1:
        return render_template('errores/errores.html', lista=datosDeVentas)
    
    posicionDeCliente = funciones.posicionDelDato('CLIENTE')
    posicionDePrecio = funciones.posicionDelDato('PRECIO')
    posicionDeCantidad = funciones.posicionDelDato('CANTIDAD')
    posicionDeCodigo = funciones.posicionDelDato('CODIGO')
    validaciones = funciones.validaciones(datosDeVentas, posicionDePrecio, posicionDeCantidad, posicionDeCodigo)


    if len(validaciones):
        return render_template('errores/errores.html', lista=validaciones)

    if formulario.validate_on_submit():
        datoIngresado = formulario.cliente.data

        cliente = datoIngresado.upper()
        posicionDelDato = funciones.posicionDelDato('CLIENTE')

        listaDeClientes = funciones.buscarDatoEspecifico(cliente, datosDeVentas, posicionDelDato)  
        return render_template('productos-por-cliente/formulario_buscar_cliente.html', form=formulario, buscarCliente=cliente, lista=listaDeClientes)
        if len(listaDeClientes) == 0:
            listaDeClientes = None
        else:
            return redirect(url_for('tablaProductoPorCliente', cliente=cliente))
    return render_template('productos-por-cliente/formulario_buscar_cliente.html', form=formulario)

@app.route('/productosxcliente/<cliente>')
def tablaProductoPorCliente(cliente):
    datosDeVentas = funciones.lecturaDeVentas()
    tablaCompleta = funciones.tablaDatosCompletos(cliente, datosDeVentas) 
    return render_template('productos-por-cliente/tabla_productorxcliente.html', cliente=cliente.title(), tabla=tablaCompleta)

@app.route('/clientesxproducto', methods=['GET', 'POST'])
def formBusquedaProducto():
    formulario = ProductoForm()
    datosDeVentas = funciones.lecturaDeVentas()
    if len(datosDeVentas) == 1:
        return render_template('errores/errores.html', lista=datosDeVentas)
    posicionDeCliente = funciones.posicionDelDato('CLIENTE')
    posicionDePrecio = funciones.posicionDelDato('PRECIO')
    posicionDeCantidad = funciones.posicionDelDato('CANTIDAD')
    posicionDeCodigo = funciones.posicionDelDato('CODIGO')
    validaciones = funciones.validaciones(datosDeVentas, posicionDePrecio, posicionDeCantidad, posicionDeCodigo)
    if len(validaciones):
        return render_template('errores/errores.html', lista=validaciones)
    if formulario.validate_on_submit():
        datoIngresado = formulario.producto.data
        producto = datoIngresado.upper()
        posicionDelDato = funciones.posicionDelDato('PRODUCTO')
        listaDeProductos = funciones.buscarDatoEspecifico(producto, datosDeVentas, posicionDelDato)
        return render_template('clientes-por-producto/formulario_buscar_producto.html', form=formulario, buscarProducto=producto, lista=listaDeProductos)
        
        if len(listaDeProductos):
            listaDeProductos = None
        else:
            return redirect(url_for('tablaClientesPorProducto', producto=producto))
    return render_template('clientes-por-producto/formulario_buscar_producto.html', form=formulario)

@app.route('/clientesxproducto/<producto>')
def tablaClientesPorProducto(producto):
    datosDeVentas = funciones.lecturaDeVentas()
    tablaCompleta = funciones.tablaDatosCompletos(producto, datosDeVentas)
    return render_template('clientes-por-producto/tabla_clientesxproducto.html', producto=producto.title(), tabla=tablaCompleta)


@app.route('/productosmasvendidos')
def productosMasVendidos():
    datosDeVentas = funciones.lecturaDeVentas()
    if len(datosDeVentas) == 1:
        return render_template('errores/errores.html', lista=datosDeVentas)
    posicionDeProducto = funciones.posicionDelDato('PRODUCTO')
    posicionDeCantidad = funciones.posicionDelDato('CANTIDAD')
    posicionDePrecio = funciones.posicionDelDato('PRECIO')
    posicionDeCodigo = funciones.posicionDelDato('CODIGO')
    validaciones = funciones.validaciones(datosDeVentas, posicionDePrecio, posicionDeCantidad, posicionDeCodigo)
    if len(validaciones):
        return render_template('errores/errores.html', lista=validaciones)
    else:
        sumaDeProductos = funciones.productosMasVendidos(datosDeVentas, posicionDeProducto, posicionDeCantidad)
        tablaCompleta = funciones.ordenarTablaDescendente(sumaDeProductos, 'PRODUCTO', 'CANTIDAD')
        return render_template('productos-mas-vendidos/productos_mas_vendidos.html', tabla=tablaCompleta)

@app.route('/mejoresclientes')
def mejoresCliente():
    datosDeVentas = funciones.lecturaDeVentas()
    if len(datosDeVentas) == 1:
        return render_template('errores/errores.html', lista=datosDeVentas)
    
    posicionDeCliente = funciones.posicionDelDato('CLIENTE')
    posicionDePrecio = funciones.posicionDelDato('PRECIO')
    posicionDeCantidad = funciones.posicionDelDato('CANTIDAD')
    posicionDeCodigo = funciones.posicionDelDato('CODIGO')
    validaciones = funciones.validaciones(datosDeVentas, posicionDePrecio, posicionDeCantidad, posicionDeCodigo)
    if len(validaciones):
        return render_template('errores/errores.html', lista=validaciones)
    else:
        sumaDePrecios = funciones.clientesQueMasCompraron(datosDeVentas, posicionDeCliente, posicionDePrecio)
        tablaCompleta = funciones.ordenarTablaDescendente(sumaDePrecios, 'CLIENTE', 'PRECIO')
        return render_template('mejores-clientes/mejores-clientes.html', tabla=tablaCompleta)

@app.route('/ingresardatos', methods=['GET', 'POST'])
def ingresarDatos():
    datosDeVentas = funciones.lecturaDeVentas()
    formulario = ingresarDatosForm()
    if len(datosDeVentas) == 1:
        return render_template('errores/errores.html', lista=datosDeVentas)
    
    posicionDeCliente = funciones.posicionDelDato('CLIENTE')
    posicionDePrecio = funciones.posicionDelDato('PRECIO')
    posicionDeCantidad = funciones.posicionDelDato('CANTIDAD')
    posicionDeCodigo = funciones.posicionDelDato('CODIGO')
    validaciones = funciones.validaciones(datosDeVentas, posicionDePrecio, posicionDeCantidad, posicionDeCodigo)
    if len(validaciones):
        return render_template('errores/errores.html', lista=validaciones)

    if formulario.validate_on_submit():
        datoDeProducto = formulario.producto.data.upper()
        datoDeCliente = formulario.cliente.data.upper()
        datoDePrecio = formulario.precio.data
        datoDeCantidad = formulario.cantidad.data
        datoDeCodigo = formulario.codigo.data.upper()
        ingreso = funciones.agregarVenta(datosDeVentas, datoDeCliente, datoDeProducto, datoDeCodigo, datoDeCantidad, datoDePrecio)
        if(ingreso):
            return render_template('formulario-ingresar-datos.html', form=formulario, mensaje=ingreso)
    return render_template('formulario-ingresar-datos.html', form=formulario)    

if __name__ == "__main__":
    # app.run(host='0.0.0.0', debug=True)
    manager.run()
