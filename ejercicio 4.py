suma = 0 
cantidad = int(input("¿Cuántos números deseas ingresar?: "))

for   i in range(cantidad):
    numero = float(input("Ingresa el número: "))
    suma = suma + numero

if cantidad > 0:
    promedio = suma / cantidad
    print("El promedio es:", promedio)
else:
    print("No se puede calcular el promedio con 0")
