import time

def calcularEdad(anioNacimiento):
    anioActual = 2026
    return anioActual - anioNacimiento

def datosPersonales(name, anioNacimiento):
    return f"Nombre: {name} \n  Tienes: {calcularEdad(anioNacimiento)} anios"

Start = time.time()

print("---------------------------------------------")
print("-----------------BIENVENIDO------------------")
print("---------------------------------------------")
name = input("Ingrese Su Nombre: ")
anioNacimiento = int(input("Ingrese su anio de nacimiento: "))

if(anioNacimiento > 2026):
    print("Error: Anio Invalido")
else:
    print("---------------------------------------------")
    print("         DATOS PERSONALES INGRESADOS         ")
    print("---------------------------------------------")
    print(datosPersonales(name, anioNacimiento))
    print("---------------------------------------------")

End = time.time()

print(f"\nTiempo Total De Ejecucion: {End - Start} Segundos")


    
    