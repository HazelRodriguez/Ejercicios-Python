#Ejercicio 3

#   Escriba un scrip que solicite al usuario digitar la contraseña para ingresar al sistema
#   (la contraseña la debe de establecer por default). Si la contraseña es incorrecta mostrar
#   en pantalla "contraseña incorrecta" ¿desa intentar nuevamente?, si la respuesta es SI,
#   el usuario tendra la posibilidad de ingresar nuevamente la contraseña; si la respuesta es No,
#   el escrip debe finalizar, si la contraseña se debe de mostrar en pantalla "Bienvenido al sistema"

#------------------------------------------------------------------------------- CODIGO ----------------------------

password = (input('Ingrese la contraseña para iniciar el sistema: \n'))
mypass = 'hazel2589'

# para este ejercicio se implemento un While que permite que el codigo se este ejecutando hasta que una de las condiciones
# se cuempla, esto hace que el codigo sea mas eficiente y presentable.

while password != mypass:
    mensaje = input('\n"Contraseña Incorrecta!"\n ¿Desea intentar nuevamente? digite (si o no)\n')
    if mensaje == "si":
        password = input('\nIngrese la contraseña: \n')
    else:
        print("\nfinalizando proceso...")
        break

if password == mypass:
    print('\n" Bienvenido al Sistema "')