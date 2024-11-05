print("-------------------------------------------------------------------------------------------")
print("Bienvenido, este programa saca el promedio entre dos temperaturas hasta que la primera sea 0")
print("-------------------------------------------------------------------------------------------")


temp1 = int(input("Ingrese la primera temperatura: "))
temp2 = int(input("Ingrese la segunda temperatura: "))

suma_temperaturas = 0
contador = 0

while True:
    if temp1 == 0:
        print("La condición se cumplió, la primera temperatura es 0.")
        break
    else:
        
        if 5 <= temp1 <= 15:
            suma_temperaturas += temp1
            contador += 1
        
       
        if 5 <= temp2 <= 15:
            suma_temperaturas += temp2
            contador += 1

        if contador > 0:
            promedio = suma_temperaturas / contador
            print(f"El promedio de las temperaturas válidas entre 5° y 15° es: {promedio:.2f}")
        else:
            print("No se ingresaron temperaturas válidas dentro del rango de 5° a 15°.")

        break


