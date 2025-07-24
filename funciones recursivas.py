def menu ():
    print("menu principal")
    print("1. factorial de un numero")
    print("2. suma de numeros naturales hasta n ")
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

def suma_numero (num):
    if num ==1:
        return 1
    else:
        return num + suma_numero(num-1)
def fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)



menu()
op=int(input("ingrese que opción desea ejecutar"))
if op==1:
    num =int(input("ingrese numero"))
    factorial(num)
    print(factorial(num))

elif op==2:
    num1=int(input("ingrese numero 1"))
    suma_numero(num1)
    print(suma_numero(num1))

elif op==3:
    num2=int(input("ingrese un  numero"))
    fibonacci(num2)
    print(fibonacci(num2))

elif op==4:
    num3=int(input("ingrese numero 3"))
elif op==5:
    num4=int(input("ingrese numero 4"))

elif op==6:
    num5=int(input("ingrese numero base"))
    num6=int(input("ingrese numero exponente"))
    potencia(num5,num6)
    print(potencia(num5,num6))

elif op==7:
    print("salir del programa")
    exit()

