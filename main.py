#Una compañia de alquiler de automoviles desea un programa para procesar los datos de los alquileres que tiene en cartera.Por cada
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


from funciones import *

def test():
    op = -1
    alquileres = []

    while op != 0:
        print('=*' * 12)
        print('MENU \n'
              '1.Cargar datos al registro'
              '\n2.Mostrar registros'
              '\n3.Cantidad de alquileres por tipo de vehiculo'
              '\n4.Buscar alquiler\n'
              '0.SALIR')
        print('=*' * 12)

        op = validar_opcion()

        if op == 1:
            tam = int(input('Ingrese la cantidad de registros a crear:'))
            alquileres = [None] * tam
            cargar(alquileres)
            print('\n EL REGISTRO SE CARGO CON EXITO!!!\n')
        elif op == 2:
            if len(alquileres) == 0:
                print('No cargo datos en el registro')
            else:
                display(alquileres)
        elif op == 3:
            if len(alquileres) == 0:
                print('No hay datos en el registro')
            else:
                vec_conteo = contar(alquileres)
                mostrar_conteo(vec_conteo)
        elif op == 4:
            if len(alquileres) == 0:
                print('No hay datos en el registro')
            else:
                print('Ingrese los datos para buscar el registro')
                c = input('Descripcion:')
                x = int(input('Cantidad de dias:'))
                pos = search(x, c, alquileres)
                if pos == -1:
                    print('No existe un registro con esos valores')
                else:
                    print('El registro buscado: \n')
                    print(write(alquileres[pos]))

    print('\nADIOS...')

if __name__ == '__main__':
    test()
