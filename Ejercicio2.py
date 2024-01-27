 #Ejercicio 2

# Escriba un scrip que muestre al usuario las siguientes opciones en un menu:
#        a. convertir libras a kilos
#        b. convertir kilos a libras
#        c. convertir euros a dolares
#        d. convertir dolares a euros
#    en base a la seleccion del usuario, el scrip debera solicitar al usuario la infirmacion necesaria
#    para realizar la conversion que haya seleccionado. finalmente debe mostrar en pantalla el resultado
#    de la conversion

#------------------------------------------------------------------------------- CODIGO ----------------------------

# Menu que se muestra al usuario
print( 'Bienvenido al sistema de conversion\n' )
print('opciones de conversion: \n'
      ' a. convertir libras a kilos\n'
      ' b. convertir kilos a libras\n'
      ' c. convertir euros a dolares\n'
      ' d. convertir dolares a euros\n'
      ' presione x para cancelar\n')
letra = (input('por favor digite la letra de la opcion de conversion que desea realizar: '))

#Opcion 'a', conversion de Lb a Kg
if letra == 'a':
 lb = float(input('Ingrese el dato equivalente a Libras (Lb): '))
 kilos = lb / 2.2
 print(lb,' lb equivale a: {:.2f}'. format(kilos),' Kg')

 #Opcion 'b', conversion de Kg a Lb
if letra == 'b':
 kg = float(input('Ingrese el dato equivalente a kilos (Kg): '))
 libras = kg * 2.2046
 print(kg, ' Kg equivale a: {:.2f}'.format(libras), ' Lb')

 #Opcion 'c', conversion de Euro a Dolar
if letra == 'c':
 eu = float(input('Ingrese la cantidad de euros: '))
 dolar = eu / 0.979
 print(eu, 'euros equivalen a: {:.2f}'.format(dolar), ' dolares americanos')

 #opcion 'd' conversion de Dolar a Euro
if letra == 'd':
 dolar = float(input('Ingrese la cantidad de Dolares: '))
 eu = dolar * 0.979
 print(dolar, 'dolares americanos equivalen a: {:.2f}'.format(eu), ' Euros')

