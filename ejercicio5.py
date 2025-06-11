print("se creara una matriz de 3x3.")
matriz= []
for i in range(3):
    fila_actual=[]
    print(f"--- Rellenando la fila {i+1} ---")
    for j in range (3):
        numero = int(input(f"Ingresa un número para la columna {j+1}:"))
    fila_actual.append(numero)




matriz.append(fila_actual) 
    
 


print("la matriz quedo asi")
for fila in matriz:
    print(fila)

positivos=0
negativos=0
ceros=0
suma_diagonal_1=0
suma_diagonal_2=0

for i in range (3):
    for j in range(3):
        numero_actual = matriz[i],[j]
        if numero_actual > 0:
            positivos +=1
        elif numero_actual < 0:
            negativos+=1
        else:
            ceros +=1

    if i==j:
        suma_diagonal_1 += numero_actual
    if i+j == 2:
        suma_diagonal_2 += numero_actual 
    
        
    

print("--- analisis culminado--")
print(f"cantidad de numeros positivos: {positivos}")
print(f"cantidad negativos: {negativos}")
print(f"cantidad de ceros: {ceros}")

print(f"La suma diagonal principal es: {suma_diagonal_1}")
print(f"la suma de la diagonal secundaria es: {suma_diagonal_2}")

if suma_diagonal_1 > suma_diagonal_2:
    print("veredicto: la diagonal principal es MAYOR.")
elif suma_diagonal_1 < suma_diagonal_2:
    print ("veredicto: la diagonal principal es MENOR.")
else:
    print("veredicto: las dos diagonales SUMAN LO MISMO.")        




