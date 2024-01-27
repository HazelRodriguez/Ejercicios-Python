#Ejercicio 4

'''Se debe >>calcular el tiempo<< que demora una persona en trasladarse de un lugar a otro,
   para ello de tiene que solicitar al usuario los datos necesarios.
   se debe de utilizar la formula de la velocidad media V = d/t'''
#  El tiempo está dado por el cociente entre la distancia recorrida y la rapidez con que se hace " t = d/v "

#------------------------------------------------------------------------------- CODIGO ----------------------------

distancia = int(input('Para calcular el tiempo escriba la distancia recorrida en numeros: \n'))
tipoDistancia = input('seleccione el tipo de distancia recorrida: \n a- km    b- M   escriba (a/b)\n')
velocidad = int(input('escriba la velocidad empleada en numeros: \n'))
tipoVelocidad = input('seleccione el tipo de velocidad empleada: \n a- km/h    b- M/s     "escriba (a/b)"\n')

tiempo = distancia/velocidad

if tipoDistancia == 'a':
    print ('EL tiempo transcurrido fue de: {:.2f}'.format(tiempo),'h')

if tipoDistancia != 'a':
    print ('EL tiempo transcurrido fue de: {:.2f}'.format(tiempo),'s')

