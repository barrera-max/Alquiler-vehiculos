from Clase import *
import random

def validar_opcion():
    num = int(input('Ingrese una opcion:'))
    while num < 0 or num > 4:
        print('ERROR...Ingrese una opcion valida')
        num = int(input('\nIngrese una opcion:'))
    return num

def cargar(vec):
    for i in range(len(vec)):
        numero = random.randint(1000,2000)
        desc = 'Auto[' + str(i+1) + ']'
        tipo = random.randint(0,9)
        importe = random.randint(5000,7800)
        dias = random.randint(1, 10)
        vec[i] = Alquiler(numero, desc, tipo, importe, dias)
    return vec

def write(vec):
    cad = 'Numero ID: {:<4} | Descripcion:{:<7} | Tipo:{:^1} | Importe:$:{:^4} | Dias de contrato:{:^3}'
    return cad.format(vec.numero, vec.desc, vec.tipo, vec.importe, vec.dias)

def display(vec):
    for i in range(len(vec)):
        print(write(vec[i]))

def contar(vec):
    conteo = [0] * 10
    for i in range(len(vec)):
        pos = vec[i].tipo
        conteo[pos] += 1
    return conteo

def mostrar_conteo(conteo):
    for i in range(len(conteo)):
        if conteo[i] != 0:
            print('Cantidad de Alquileres del Tipo[' + str(i) +']:', conteo[i])

def search(x,c, vec):
    for i in range(len(vec)):
        if vec[i].desc == c and vec[i].dias == x:
            return i
    return -1