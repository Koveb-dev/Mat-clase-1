import time
import os


def esperar_limpiar_screen():
    time.sleep(1)
    os.system('cls')


def celsius_fahrenheit():
    while True:
        try:
            c_f = float(
                input('Ingrese los grados Celsius a convertir en Fahrenheit: '))
            break
        except:
            print('ERROR! debe ingresar un numero!')

    conversion_fahrenheit = 9/5 * c_f + 32

    conversion_fahrenheit = round(conversion_fahrenheit, 2)
    print(f'{c_f}º Celsius equivalen a {conversion_fahrenheit}º Fahrenheit')


celsius_fahrenheit()
