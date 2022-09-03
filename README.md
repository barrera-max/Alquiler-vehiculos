# Alquiler-vehiculos
Ejercicio de la materia Algoritmos y Estructuras de Datos
Los registros se cargan de manera automatica y con valores aleatorios usando la libreria random.
Uso del algoritmo basico de busqueda y un menu de opciones.
Las opciones ingresadas por teclado por el usuario se validan.

ENUNCIADO:

Una compañia de alquiler de automoviles desea un programa para procesar los datos de los alquileres que tiene en cartera.Por cada
#operacion de alquiler realizada se tienen los siguientes datos: el numero de id de la operacion, la descripcion del automovil
#el tipo de automovil(un numero entero entre 0 y 9, para indicar 0:sedan cuatro puertas, 1: familiar siete asientos,etc),
#el importe a cobrar por el alquiler y la cantidad de dias por los que se hace el alquiler.Se desea almacenar la informacion
#referida a los n alquileres en un arreglo de registros de tipo Alquiler(definir el tipo Alquiler y cargar n por teclado)
#
# Se pide desarrollar un programa en Python controlado por un menu de opciones, que permita gestionar las siguientes tareas:
# 1- Cargar el arreglo pedido con los datos de los n alquileres. Valide que el numero ID de la operacion de alquiler sea positivo
# y que el tipo del vehiculo este entre 0 y 9. Puede hacer la carga en forma manual, o puede generar los datos en forma automatica
# (con valores aleatorios) o puede disponer de ambas tecnicas.
# 2. Mostrar los datos de todos los alquileres, en un listado ordenado de menor a mayor segun los importes a cobrar.
# 3. Determinar y mostrar la cantidad de alquileres que se hicieron de cada tipo posible de vehiculo(un contador para los alquileres
# de vehiculos tipo 0, otro para tipo 1, etc) En total, 10 contadores usando un vector de conteo.
# 4- Determinar si fue alquilado un vehiculo cuya descripcion sea igual a c y que haya sido alquilado por X cantidad de dias o mas,
# siendo c y X dos valores que se ingresan por teclado, Si existe, mostrar
