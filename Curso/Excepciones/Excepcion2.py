def division():
    try:
        op1 = (float(input("Introduce el primer numero: ")))
        op2 = (float(input("Introduce el segundo numero: ")))

        print("La division es: " + str(op1/op2))

    except ValueError:
        print ("El valor introducido no es correcto")
    except ZeroDivisionError:
        print ("No se puede dividir por cero")
    finally:
        print("Calculo realizado.")

division()