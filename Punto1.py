
cont1 = 0
cont2 = 0
cont3 = 0
n = int(input('Digite la cantidad de numeros que desea ingresar : '))

for i in range (n) :
    num = int(input('Digite el numero que desea ingresar :'))
    if(num % 2 == 0 and num % 3 == 0):
        cont1 += 1
    elif(num % 2 == 0) :
        cont2 += 1
    elif(num % 3 == 0) :
        cont3 += 1  
print(f"El numero de veces que se ingreso un numero multiplo de 2 y multiplo de 3 es : {cont1}")
print(f"El numero de veces que se ingreso un numero multiplo de 2 es : {cont2}")
print(f"El numero de veces que se ingreso un numero multiplo de 3 es : {cont3}")
    