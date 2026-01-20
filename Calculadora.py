# Calculadora.py
WIDTH = 80
import os
def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")

print("\n")
print(str.center("----------------------------------", WIDTH))
print(str.center("Bienvenido a la calculadora simple", WIDTH))
print(str.center("----------------------------------", WIDTH) + "\n")

while True:
    print(str.center("Seleccione la operacion que desea realizar:", WIDTH))
    print(str.center("1. Suma de números", WIDTH))
    print(str.center("2. Producto entre números", WIDTH))
    print(str.center("3. División entre 2 números", WIDTH))
    print(str.center("4. Factorial de un número", WIDTH))
    print(str.center("5. Tabla de multiplicar", WIDTH))
    print(str.center("6. Calculo del cuadrado y cubo de un número", WIDTH))
    print(str.center("7. Promedio de una serie de numeros", WIDTH))
    print(str.center("8. Maximo y minimo de n numeros", WIDTH))

    print()
    prompt = ("Ingrese el numero de la operacion (1/2/3/4/5/6/7/8):")
    opcion = input(prompt)
    match opcion:
        case "1":
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))
            resultado = num1 + num2
            if resultado.is_integer():
                print(str.center(f"El resultado de la suma es: {int(resultado)}", WIDTH) + "\n") # Si el resultado es un entero, lo muestra sin decimales
            else:
                print(str.center(f"El resultado de la suma es: {resultado}", WIDTH) + "\n") # Si no, lo muestra con decimales
        case "2":
            n = int(input("Cuántos numeros desea multiplicar?: "))
            producto = 1

            for i in range(1, n + 1):
                num = float(input(f"Ingrese el numero {i}: "))
                producto *= num

            if producto.is_integer():
                print(str.center(f"El producto total es: {int(producto)}", WIDTH) + "\n")
            else:
                print(str.center(f"El producto total es: {producto}", WIDTH) + "\n")

        case "3":
            num1 = float(input("Ingrese el primer número"))
            num2 = float(input("Ingrese el segundo número"))
            res = num1 / num2
            print(str.center(f"El resultado de la división es: {res}",WIDTH)+ "\n" )

        case "4":
            n = int(input("Ingrese un numero entero para calcular su factorial: "))

            if n < 0:
                print(str.center("El factorial no está definido para numeros negativos.", WIDTH) + "\n")
            else:
                factorial = 1
                for i in range(1, n + 1):
                    factorial *= i

                print(str.center(f"El factorial de {n} es: {factorial}", WIDTH) + "\n")

        case "5":
            num = int(input("Ingrese el numero de la tabla de multiplicar: "))
            print()

            for i in range(1, 11):
                resultado = num * i
                print(str.center(f"{num} x {i} = {resultado}", WIDTH))

            print()

        case "6":
            num = float(input("Ingrese un número: "))
            cuadrado = num ** 2
            cubo = num ** 3

            print(str.center(f"El cuadrado de {num} es: {cuadrado}", WIDTH))
            print(str.center(f"El cubo de {num} es: {cubo}", WIDTH) + "\n")

        case "7":
            suma = 0
            contador = 0

            print("Ingrese números para calcular el promedio (-1 para terminar):")

            while True:
                num = float(input("Ingrese un numero: "))
                if num == -1:
                    break
                suma += num
                contador += 1

            if contador == 0:
                print(str.center("No se ingresaron numeros para calcular el promedio.", WIDTH) + "\n")
            else:
                promedio = suma / contador
                if promedio.is_integer():
                    print(str.center(f"El promedio es: {int(promedio)}", WIDTH) + "\n")
                else:
                    print(str.center(f"El promedio es: {promedio}", WIDTH) + "\n")

        case "8":
            n = int(input("Cuantos numeros enteros desea ingresar?: "))

            if n <= 0:
                print(str.center("La cantidad debe ser mayor a cero.", WIDTH) + "\n")
            else:
                num = int(input("Ingrese el numero 1: "))
                maximo = num
                minimo = num

                for i in range(2, n + 1):
                    num = int(input(f"Ingrese el numero {i}: "))
                    if num > maximo:
                        maximo = num
                    if num < minimo:
                        minimo = num

                    print(str.center(f"Valor maximo: {maximo}", WIDTH))
                    print(str.center(f"Valor minimo: {minimo}", WIDTH))
                    print(str.center(f"Total de valores ingresados: {n}", WIDTH) + "\n")

    while True:
        repetir = input("Desea realizar otra operacion? (s/n): ").lower()
        if repetir == "s":
            limpiar_pantalla()
            break
        elif repetir == "n":
            print(str.center("Gracias por usar la calculadora. Hasta luego!", WIDTH) + "\n")
            exit()
        else:
            print("Entrada invalida. Por favor ingrese 's' o 'n'.")
        