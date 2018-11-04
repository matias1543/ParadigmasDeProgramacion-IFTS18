Informe del programa HoneyBee

#lecturaDeVentas
	Utilizada para la lectura del archivo.

#posicionDelDato
	Retorna el índice donde se encuentra el titulo en el archivo csv.

#buscarDatoEspecifico
	En ésta función se busca la posición del dato ingresado.

#tablaDatosCompletos
	Se muestran los datos dentro de la tabla.

#ordenarMayorAMenor
	Ordenamiento de los datos a través de producto y cantidad.
    Se devuelven de mayor a menor.

#productosMasVendidos
	Informe de los resultados sobre los productos mas vendidos.

#ordenarMayorAMenorPecios
	Ordenamiento de los datos de mayor a menor (Cliente y Precio).

#clientesQueMasCompraron
	Se muestran los clientes que más compraron, con la cantidad total gastada.

#Validaciones
    En esta función se indicara las validaciones necesarias para las columnas CODIGO, CANTIDAD y PRECIO.    
#Aclaración
	Se crearon 2 clases en el archivo forms.py, (ClienteForm, ProductoForm) para poder ingresar cliente, e ingresar producto.

#¿Qué estructura se utilizará para representar la información del archivo?
La información del archivo se muestra estructurada en forma de tabla, la cuál posee 4 pestañas distintas, usadas para informar al usuario los distintos tipos de consultas que se pueden realizar. 

#Como se usa el programa:

#1
	Una vez dentro del sistema, estaremos situados en la pantalla de inicio, y prodremos ver la barra de navegación, la cuál sirve para poder realizar consultas.
#2
	En la solapa 'Lista completa' podemos cliquear para que nos muestre la tabla completa de las compras realizadas por clientes.
#3
	En productos por clientes, podremos buscar un cliente, y se mostrarán todos los productos adquiridos por dicho cliente buscado.
#4
	La sección de clientes por producto, permite filtrar, pero en éste caso se filtra por producto. Una vez se busca el producto, se muestran todos los clientes que compraron el producto seleccionado.
#5
	En la parte de 'productos más vendidos' podemos visualizar una tabla de los productos más vendidos con la cantidad total y nombre del producto. 
#6
	Por último, en la consulta ‘Mejores Clientes’ se muestran los clientes que más productos compraron. Se informa el nombre de cada cliente y el precio total de los productos que adquirió.