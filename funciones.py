import csv

#Funcion que devuelve en forma de lista el archivo csv. 
#Valida en caso de que no exista el archivo o le falten campos.
def lecturaDeVentas():
    cantidaDeCampos = 5
    datosDeVentas = []

    try:
        with open("examen.csv") as archivo:
            archivo_csv = csv.reader(archivo)
            dato = next(archivo_csv, None)
            while dato:
                datosDeVentas.append(dato)
                dato = next(archivo_csv, None)
        for linea in datosDeVentas:
            if len(linea) != cantidaDeCampos:
                datosDeVentas = [["El archivo csv no contiene todos los campos."]]
                break
    except:
        datosDeVentas.append(["El archivo csv no existe."])
    return datosDeVentas

#Función que retorna el indice donde se encuentra el titulo (osea de la primera fila del archivo)
def posicionDelDato(titulo):
	dato = lecturaDeVentas()
	posicion = dato[0].index(titulo)
	return posicion

#Función que filtra la lista con un dato especifico y retorna una lista de los datos cercanos a ese filtro.
def buscarDatoEspecifico(datoEspecifico, datosDeVenta, posicionDelDato):
    listaDatos = []
    for linea in datosDeVenta[1:]:
        if datoEspecifico in linea[posicionDelDato] and linea[posicionDelDato] not in listaDatos:
            listaDatos.append(linea[posicionDelDato])
    return listaDatos

#Función que retorna retorna una determinada lista usando como filtro un dato especifico
def tablaDatosCompletos(datoEspecifico, datosDeVenta):
    filasAMostrar = []

    #Recorre la primera fila de la lista (Titulos) que se almacenara en filasAMostrar
    for titulos in datosDeVenta[:1]:
            filasAMostrar.append(titulos)


    for linea in datosDeVenta[1:]:
        for dato in linea:
            if dato == datoEspecifico:
                filasAMostrar.append(linea)
    return filasAMostrar

#Función que ordena de mayor a menor la lista.
def ordenarTablaDescendente(tabla, posicionDeColumna1, posicionDeColumna2):
    lista = []
    listaOrdenada = []
    tablaAMostrar = [[posicionDeColumna1, posicionDeColumna2]]
    posicion = tablaAMostrar[0].index(posicionDeColumna2)

    #Recorre la que se desea ordenar
    for linea in tabla:
        lista.append(linea[posicion])
    
    lista.sort() #Con el metodo sort se ordena de menor a mayor
    #Recorre la lista ordenada para guardarlo en una lista nueva de mayor a menor 
    for i in reversed(lista):
        listaOrdenada.append(i)
    
    #Recorre la lista (Ord.de Mayo a menor) donde servira como filtro para ordenar la tabla que deseamos de mayor a menor.
    for i in listaOrdenada:
        for linea in tabla:
            for dato in linea:
                if dato == i:
                    tablaAMostrar.append(linea)
    return tablaAMostrar

#Función que retorna una lista de los productos mas vendidos
def productosMasVendidos(datosDeVenta, posicionDeProducto, posicionDeCantidad):
    listaProductos = []
    tabla = []

    #Recorre la lista del archivo csv para obtener solo los titulos requeridos, en este caso PRODUCTO y CANTIDAD
    for linea in datosDeVenta[1:]:
        if linea[posicionDeProducto] not in listaProductos:
            listaProductos.append(linea[posicionDeProducto])
    
    #Recorre la lista de productos, en caso de que se repita el producto en el recorrido suma las cantidades guardando en una lista nueva el producto y el total de cantidad.
    for producto in listaProductos:
        cantidad = 0
        for linea in datosDeVenta[1:]:
            if linea[posicionDeProducto] == producto:
                cantidad = cantidad + int(linea[posicionDeCantidad])
            nuevaLista = [producto, cantidad]
        tabla.append(nuevaLista)
    return tabla
 
#Función que retorna una lista de los mejores clientes.
def clientesQueMasCompraron(datosDeVenta, posicionDeCliente, posicionDePrecio):
    listaClientes = []
    tabla = []
    
    #Recorre la lista del archivo csv para obtener solo los titulos requeridos, en este caso CLIENTE y PRECIO
    for linea in datosDeVenta[1:]:
        if linea[posicionDeCliente] not in listaClientes:
            listaClientes.append(linea[posicionDeCliente])

    #Recorre la lista de clientes, en caso de que se repita el cliente en el recorrido suma los gastos guardando en una lista nueva el cliente y el total que gasto.
    for cliente in listaClientes:
        precio = 0
        for linea in datosDeVenta[1:]:
            if linea[posicionDeCliente] == cliente:
                precio = precio + float(linea[posicionDePrecio])
            nuevaLista = [cliente, round(precio, 2)]
        tabla.append(nuevaLista)
    return tabla

#Función que valida todas las filas de la Columa CODIGO, PRECIO y CANTIDAD
def validaciones(datosDeVenta, posicionDePrecio, posicionDeCantidad, posionDeCodigo):
    fila = 1
    cantCampos = 5
    errores = []
    limiteCodigo = 6
    
    #Validacion en caso de que haya enteros en la columna de PRECIO
    for linea in datosDeVenta[1:]:
        flotante = linea[posicionDePrecio].count('.')
        if flotante == 0:
            errores.append(['La columna PRECIO en la fila {} no puede tener números enteros.'.format(fila)])
        fila = fila + 1
        flotante = 0
    fila = 1
    #Validacion en caso de que haya flotantes en la columna de CANTIDAD
    for linea in datosDeVenta[1:]:
        entero = linea[posicionDeCantidad].count('.')
        if entero == 1:
            errores.append(['La columna CANTIDAD en la fila {} no puede tener números flotantes.'.format(fila)])
        fila = fila + 1
        entero = 0
    fila = 1
    #Validaciones en caso de que haya mas o menos de 6 caracteres.
    #Validaciones en caso de los 3 primeros caracteres no sean letras.
    #Validaciones en caso de los 3 ultimos caracteres no sean números.
    for linea in datosDeVenta[1:]:
        cont = 0
        while cont < len(linea[posionDeCodigo]):
            if cont >= limiteCodigo:
                errores.append(['La columna CODIGO en la fila {} no puede tener mas de 6 caracteres.'.format(fila)])
            elif len(linea[posionDeCodigo]) < 6:
                errores.append(['La columna CODIGO en la fila {} no puede tener menos de 6 caracteres.'.format(fila)])
                cont = len(linea[posionDeCodigo])
            elif cont < 3:
                if linea[posionDeCodigo][cont].isdigit():
                    errores.append(['La columna CODIGO en la fila {} no puede tener números en los primeros 3 caracteres.'.format(fila)])
            elif cont >=3 and cont < limiteCodigo:
                if linea[posionDeCodigo][cont].isdigit() == False:
                    errores.append(['La columna CODIGO en la fila {} no puede tener letras en los ultimos 3 caracteres.'.format(fila)])
            cont = cont + 1
        fila = fila + 1
    return errores

def agregarVenta(listaVentas, cliente, producto, codigo, cantidad, precio):
    datosAIngresar = []
    
    for titulos in listaVentas[:1]:
        for titulo in titulos:
            if titulo == 'PRODUCTO':
                datosAIngresar.append(producto)
            elif titulo == 'CLIENTE':
                datosAIngresar.append(cliente)
            elif titulo == 'CANTIDAD':
                datosAIngresar.append(str(cantidad))
            elif titulo == 'PRECIO':
                datosAIngresar.append(str(precio))
            elif titulo == 'CODIGO':
                datosAIngresar.append(codigo)
    
    data = ','.join(datosAIngresar)

    try:
        with open('examen.csv', 'a') as archivo:
            archivo.write("\n{}".format(data))
        return True
    except:
        return False