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
    print(str.center("1. Suma", WIDTH))
    print(str.center("2. Resta", WIDTH))
    print(str.center("3. Multiplicacion", WIDTH))
    print(str.center("4. Division", WIDTH))
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
        