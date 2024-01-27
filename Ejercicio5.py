# Ejercicio 5

# Escriba un Scrip que sea capaz de calcular el índice de masa corporal de una persona
# en base a los datos ingresados del usuario. (Formula del IMC es: IMC = peso(Kg)/Estatura(m2))

# ------------------------------------------------------------------------------- CODIGO ----------------------------

Peso = float(input('Bienvenido al sistema!!!\nPara poder calcular el índice de su masa corporal (IMC) ingrese su peso '
                   'en Kilogramos (Kg): \n'))

Estatura = float(input('Ingrese su altura: \n'))

IMC = Peso / (Estatura * Estatura)

print('Su índice de Masa Corporal (IMC) es: {:.2f}'.format(IMC))

print('\nEn la siguiente tabla podra verificar su peso o Composicion corporal, segun su IMC \n'
      '\n ["Composicion corporal"]___|______["IMC"]_____\n'
      ' |      -Peso Bajo          |    Menos de 18.5|\n'
      ' |      -Peso Normal        |    18.5  -  24.9|\n'
      ' |      -Sobre peso         |    25.0  -  29.9|\n'
      ' |      -Obesidad           |    Más de 30.0  |\n')

