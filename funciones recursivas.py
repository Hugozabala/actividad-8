def menu ():
    print("menu principal")
    print("1. factorial de un numero")
    print("2. suma de dos numeros")
    print("3. fibonacci de un numero")
    print("4. cuantas veces aparece una letra en una palabra")
    print("5. invertir una cadena")
    print("6. calcular la potencia de un numero")
    print("7. salir")


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
menu()
op=int(input("ingrese que opción desea ejecutar"))
if op==1:
    num =int(input("ingrese numero"))
    factorial(num)
    print(factorial(num))



