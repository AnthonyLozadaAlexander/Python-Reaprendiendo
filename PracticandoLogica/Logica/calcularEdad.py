import time

def calcularEdad(anioNacimiento):
    anioActual = 2026
    return anioActual - anioNacimiento


Start = time.time()
print("----------------------------------------------")
print("-----------------BIENVENIDO-------------------")
print("----------------------------------------------")
on = False
while(not on):
    anioNacimiento = int(input("Ingrese Su Anio De Nacimiento: "))
    if(anioNacimiento > 2026):
        print("Error: Anio Invalido") 
        on = False
    edad = calcularEdad(anioNacimiento)
    match edad:
        case edad if edad > 0 and edad < 18: 
            print("Eres Menor De Edad")
            on = True
        case edad if edad >= 18 and edad <= 65: 
            print("Eres Mayor De Edad")
            on = True
        case edad if edad > 65: 
            print("Estas en edad de jubilacion")
            on = True
        case _: 
            print("Error: Edad Invalida")
            on = False
                  

print("----------------------------------------------")
print("Cerrando Programa")
End = time.time()

print(f"\nTiempo Total De Ejecucion: {End - Start} Segundos")