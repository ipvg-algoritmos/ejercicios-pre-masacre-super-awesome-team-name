lista = [1,2,3,4,5,6,7,8,9,10]
num = int(input("Seleccione el numero que desea buscar: "))

for i in lista:
    if i == num:
        print(f"El numero se encuentra en la lista y su posicion es numero es: {i}")
    else:
        print(f"El numero {num} no existe en la lista")
        break
