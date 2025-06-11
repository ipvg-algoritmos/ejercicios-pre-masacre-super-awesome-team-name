lista =[]
while True:
    num = int(input("Escribe aqui el numero, para finalizar escriba un numero negativo: "))
    if num < 0:
        break
    else:
        lista.append(num)

print(f"""El numero mayor de la lista es: {max(lista)}
El numero menor de la lista es: {min(lista)}""")




   
