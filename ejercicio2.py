frase= input("crea una frase:")
vocales= "aeiou"
num_vocales=0
num_consonantes=0
for letra in frase.lower():
    if letra.isalpha ():
        if letra in vocales:
             num_vocales +=1
    
else:
    num_consonantes +=1 

print("n------Ya esta contado------")
print(f"en tu frase encontraste {num_vocales} vocales")
print(f"tambien hay {num_consonantes} consonantes")