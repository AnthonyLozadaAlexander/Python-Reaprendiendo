

def sumatoria(num):
    if num == 1:
        return 1
    else:

        return num + sumatoria(num - 1)


print("--------Bienvenido a la sumatoria recursiva--------")
num = int(input("Ingrese un numero: "))
print(f"N ingresado: {num}")
print(f"La sumatoria total es: {sumatoria(num)}")