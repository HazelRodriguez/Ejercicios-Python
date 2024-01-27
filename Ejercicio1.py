#Ejercicio 1

''' Su escript debe solicitar al usuario digitar la cantidad de calificaciones que desea
    ingresar y de las que calculara un promedio final. El scrip debera de solicitar cada
    una de las calificaciones y finalmente imprimira el promedio final'''

#------------------------------------------------------------------------------- CODIGO ----------------------------

# cn = Cantidad de Notas a Ingresar.

cn = int(input('digite el numero de calificaciones que desea ingresar:'))
lista = []  #este apartado tiene la finalidad de llevar el control de las notas que se van ingresando (funcion de lista)
position = 1
notasIngresadas = cn

while cn > 0:
    nota = float(input('Ingrese la calificación {}: '.format(position)))
    lista.append(nota)
    cn -=1
    position +=1

   # print(lista) este codigo permite ir mostrando los datos de la lista en este caso las notas

    # El siguiente codigo realiza la suma de las notas e imprime el promedio final de las notas ingresadas,
    # para ello se implemento un for

    sumaNotas = 0
    for os in lista:
        sumaNotas = sumaNotas + os

    promedio = round(sumaNotas/notasIngresadas)

    #Imprimiendo en pantalla
    print('el promedio de la nota ingresada es: {}'. format(promedio))