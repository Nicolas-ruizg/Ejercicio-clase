
print ("-------------------------------------------------------------------------------------------")
print("Bienvenido, este programa saca el promedio entre dos temperaturas hasta que la primera sea 0")
print ("-------------------------------------------------------------------------------------------")
temp1=(int(input("ingrese la primera temperatura: ")))
temp2=(int(input("ingrese la segunda temperatura: ")))

while True:
    if temp1 == 0:
        print("La condicion se cumplio, la primera temperatura es 0 ")
        break
    else:
        suma=temp1+temp2
        promedio=suma/2
        print("El promedio de las temperaturas es:",promedio)
        break