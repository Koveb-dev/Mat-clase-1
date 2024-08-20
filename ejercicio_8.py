import time
import os
import random


def esperar_limpiar_screen():
    time.sleep(1)
    os.system('cls')


lista = []

for x in range(10):
    lista.append(random.randint(1, 100))


print('Numeros generados: ', lista)
print(
    f'El segundo elemento de la lista es: {lista[1]}\nEl sexto elemento de la lista es: {lista[5]}')
