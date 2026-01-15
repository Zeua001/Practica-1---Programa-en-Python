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
    print(str.center("5. Salir", WIDTH))
    print()
    prompt = ("Ingrese el numero de la operacion (1/2/3/4/5):")
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
        case "4":
            n = int(input("Ingrese un numero entero para calcular su factorial: "))

            if n < 0:
                print(str.center("El factorial no está definido para numeros negativos.", WIDTH) + "\n")
            else:
                factorial = 1
                for i in range(1, n + 1):
                    factorial *= i

                print(str.center(f"El factorial de {n} es: {factorial}", WIDTH) + "\n")

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
        