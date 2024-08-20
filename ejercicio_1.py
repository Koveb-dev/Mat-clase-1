import time
import os


def esperar_limpiar_screen():
    time.sleep(1)
    os.system('cls')


while True:
    try:
        num = float(input('Ingrese un número: '))
        if num == 0:
            print('El numero ingresado es cero!')
            esperar_limpiar_screen()
            break
        elif num > 0:
            print(f'El numero ingresado {num} es positivo!')
            esperar_limpiar_screen()
            break
        else:
            print(f'El numero ingresado {num} es negativo!')
            esperar_limpiar_screen()
            break
    except:
        print('ERROR! debe ingresar un numero no letras ni otro tipo de dato!')
