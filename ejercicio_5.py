import time
import os


def esperar_limpiar_screen():
    time.sleep(1)
    os.system('cls')


while True:
    try:
        num = int(input('Ingrese un numero entero: '))
        if num != 0:
            print('Numero entero ingresado correctamente!')
            esperar_limpiar_screen()
            break
        else:
            print('No puede ingresar 0!')
            esperar_limpiar_screen()
    except:
        print('ERROR! debe ingresar un número entero!')

print('Tabla de multiplicacion del 1 al 12 de un numero entero!')
for x in range(1, 13):
    print(f'{num} x {x} es igual: {num*x}')
