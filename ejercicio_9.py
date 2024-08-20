
import time
import os


def esperar_limpiar_screen():
    time.sleep(1)
    os.system('cls')


def calcular_imc():
    while True:
        try:
            peso = float(input('Ingrese su peso(kg): '))
            if peso >= 10:
                print('Peso ingresado correctamente!')
                esperar_limpiar_screen()
                break
            else:
                print('ERROR! debe ingresar un peso superior o igual a 10kg!')
        except:
            print('ERROR! debe ingresar números!')

    while True:
        try:
            altura = int(
                input('Ingrese su altura en centimentros, si mide 1.67 ingrese (167cm): '))
            if altura >= 100:
                print('Altura ingresada correctamente!')
                esperar_limpiar_screen()
                altura = altura / 100
                break
            else:
                print('ERROR! la altura minima es de 1 metro!')
            esperar_limpiar_screen()
        except:
            print('ERROR! debe ingresar números!')

    imc = round(peso / (altura)**2, 2)

    if imc < 18.5:
        print('Bajo peso, su imc es {imc}!!')
    elif imc >= 18.5 and imc <= 24.9:
        print(f'Peso normal, su imc es {imc}!')
    elif imc >= 25 and imc <= 29.9:
        print(f'Sobrepeso, su imc es {imc}!')
    else:
        print(f'Obesidad, su imc es {imc}!')


calcular_imc()


lista_estudiantes_imc = [16.43, 19.31, 10.25, 18.63,
                         17.85, 19.76, 23.64, 21.94, 21.3, 22.67, 16.48]

for x in lista_estudiantes_imc:
    if x < 18.5:
        posicion = lista_estudiantes_imc.index(x)
        print(
            f'El estudiante de la posicion {posicion+1} de la lista con un imc de {x}kg esta bajo peso!')
