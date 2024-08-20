import time
import os


def esperar_limpiar_screen():
    time.sleep(1)
    os.system('cls')


x = 0

for i in range(2, 101):
    x += 1
    print(f'La suma de {x} + {i} es: {x+i}')
