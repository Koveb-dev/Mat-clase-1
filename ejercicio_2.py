import time
import os


def esperar_limpiar_screen():
    time.sleep(1)
    os.system('cls')


while True:
    try:
        num = int(input('Ingrese un número entero: '))
        if num % 2 == 0:
            print(f'El numero {num} es par!')
            esperar_limpiar_screen()
            break
        else:
            print(f'El numero {num} es impar!')
            esperar_limpiar_screen()
            break
    except:
        print('ERROR! debe ingresar un numero entero!')
