import time
import os


def esperar_limpiar_screen():
    time.sleep(1)
    os.system('cls')


contra_correcta = "Contraseña"

while True:
    contra = str(input('Ingrese la contraseña: '))
    contra = contra.replace(" ", "")
    if contra.capitalize() == contra_correcta:
        print('Contraseña correcta!')
        esperar_limpiar_screen()
        break
    else:
        print('Contrasena incorrecta, vuelva a intentarlo por favor!')
        esperar_limpiar_screen()
