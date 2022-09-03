
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
