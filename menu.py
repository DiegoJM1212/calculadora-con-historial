def pedir_numero(mensaje):
   while True:
      try:
         return int(input(mensaje))
      except ValueError:
         print("error: solo se permiten numeros enteros")

def suma():
    num1 =pedir_numero("ingrese el primer numero")
    num2 = pedir_numero("ingrese el segundo numero")
    resultado = (num1 + num2)
    historial.append(f"{num1} + {num2} = {resultado}")
    print("el resultado de la suma es: ", resultado)


def resta():
    num1 =pedir_numero("ingrese el primer numero")
    num2 = pedir_numero("ingrese el segundo numero")
    resultado = (num1 - num2)
    historial.append(f"{num1} - {num2} = {resultado}")
    print("el resultado de la resta es: ", resultado)


def multiplicacion():
    num1 =pedir_numero("ingrese el primer numero")
    num2 = pedir_numero("ingrese el segundo numero")
    resultado = (num1 * num2)
    historial.append(f"{num1} * {num2} = {resultado}")
    print("el resultado de la multiplicacion es: ", resultado)

def division():
        num1 =pedir_numero("ingrese el primer numero")
        num2 = pedir_numero("ingrese el segundo numero")
        if num2 == 0:
          print("no se puede dividir entre 0")
        else:
            resultado = (num1 / num2)
            historial.append(f"{num1} / {num2} = {resultado}")
            print("el resultado de la division es:", resultado)

historial = []
def mostrar_historial():
    for x in historial:
        print(x)


opciones = 1
while opciones !=6:
    print("1.suma \n2.resta \n3.multiplicacion \n4.division \n5.historial \n6.salir")
    while True:
       try:
           opciones = int (input ("ingresar una opcion: "))
           break
       except ValueError:
           print("error: ingrese un numero valido")

    if opciones ==1:
       suma()
    elif opciones ==2:
        resta()
    elif opciones ==3:
         multiplicacion()
    elif opciones ==4:
         division()
    elif opciones ==5:
        mostrar_historial()
    elif opciones ==6:
         print ("saliste del sistema cerrando programa")
    else:
      print("ingresa una opcion valida")
