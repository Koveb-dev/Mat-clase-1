import time
import os


def esperar_limpiar_screen():
    time.sleep(1)
    os.system('cls')


def dos_num_y_producto():
    while True:
        try:
            num1 = float(input('ingrese un numero: '))
            break
        except:
            print('ERROR! debe ingresar un numero, no letras o caracteres!')

    while True:
        try:
            num2 = float(input('ingrese un segundo numero: '))
            break
        except:
            print('ERROR! debe ingresar un numero, no letras o caracteres!')

    producto = num1 * num2
    return producto


def redondeo(producto):
    return int(producto)


producto_numeros = dos_num_y_producto()

redondeo_numeros = redondeo(producto_numeros)

print("El resultado de la multiplicacion y el redondeo de los dos números es: ", redondeo_numeros)
